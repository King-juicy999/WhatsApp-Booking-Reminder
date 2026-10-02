# WhatsApp Booking Reminder

A WhatsApp bot that takes bookings and sends automatic reminders before each appointment.

A business registers itself, lists the services it offers, and its customers book
appointments against those services. Each booking gets a reminder scheduled ahead of
time, and the bot sends it over WhatsApp so nobody misses their appointment.

## Status

Early build. The data model, the Django configuration and a REST API around the core
records are written and working. The WhatsApp integration and the reminder sending are
not built yet.

This section is the honest part of this file. Everything below it describes code that
exists.

### What works

- The four apps and their models, registered in Django admin.
- A REST API for businesses, customers, services and appointments.
- Django, PostgreSQL, Redis and Celery configuration, all driven by environment
  variables.

### What is stubbed or missing

- **The `whatsapp` app is empty.** It has an `AppConfig` and nothing else. No webhook,
  no client, no message sending.
- **No reminders are ever sent.** `reminders` has a `Reminder` model and admin, but no
  Celery tasks exist to find due reminders or deliver them. `autodiscover_tasks()` is
  configured and currently finds nothing, because no app has a `tasks.py`.
- **The API has no authentication.** Every endpoint is open to anyone who can reach the
  server. Queries are not scoped per business either, so the API returns every
  business's customers and appointments. Both need to close before this is deployed
  anywhere public.
- **No migrations have been run.** There are no `migrations/` directories yet, so the
  database schema does not exist until `makemigrations` and `migrate` are run.
- **`WHATSAPP_API_URL` and `WHATSAPP_API_TOKEN`** are read into settings but nothing
  reads them from there yet. They are reserved for the WhatsApp client.
- **There are no tests.** Nothing is checked automatically.
- **`templates/` does not exist**, though `TEMPLATES['DIRS']` points at it. Django
  tolerates the missing directory.

## Requirements

Python 3, PostgreSQL, and Redis if you intend to run the worker.

```
pip install -r requirements.txt
```

Django, Django REST Framework, psycopg2-binary, Celery, redis and python-dotenv.

## Configuration

Copy the example file to `.env` and fill it in. Every setting falls back to a sensible
local default, so the app boots without a `.env` at all.

```
cp .env.example .env
```

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Django secret key. Change this. |
| `DEBUG` | `True` for local work, `False` anywhere else. |
| `ALLOWED_HOSTS` | Comma separated host list. |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | PostgreSQL connection. |
| `CELERY_BROKER_URL` | Redis broker, defaults to `redis://localhost:6379/0`. |
| `CELERY_RESULT_BACKEND` | Redis results, defaults to `redis://localhost:6379/1`. |
| `WHATSAPP_API_URL`, `WHATSAPP_API_TOKEN` | Reserved for the WhatsApp client. |

`.env` is gitignored. Never commit it.

## Running it

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The admin is at `/admin/`. The API is under `/api/`.

The Celery worker, once there are tasks to run:

```
celery -A config worker
```

## The API

Every endpoint is a function-based view using DRF's `@api_view`, no ViewSets. All of
them are open and unscoped, see the status section above.

### Businesses

| Method | Path | Name |
|---|---|---|
| GET, POST | `/api/businesses/` | `business_list_create` |
| GET, PUT, PATCH, DELETE | `/api/businesses/<id>/` | `business_detail` |

### Customers

| Method | Path | Name |
|---|---|---|
| GET, POST | `/api/customers/` | `customer_list_create` |
| GET, PUT, PATCH, DELETE | `/api/customers/<id>/` | `customer_detail` |

### Appointments

| Method | Path | Name |
|---|---|---|
| GET, POST | `/api/appointments/` | `appointment_list_create` |
| GET, PUT, PATCH, DELETE | `/api/appointments/<id>/` | `appointment_detail` |
| GET, POST | `/api/appointments/services/` | `service_list_create` |
| GET, PUT, PATCH, DELETE | `/api/appointments/services/<id>/` | `service_detail` |

`POST` returns 201 on success and 400 with the field errors otherwise. Detail routes
return 404 for a missing id, 204 on delete, and 200 on a successful read or write.

Foreign keys are plain integers on input, so creating a customer takes
`{"business": 1, "name": "Sam", "phone_number": "447700900123"}`.

## The models

**`businesses.Business`** is the tenant root. Name, WhatsApp number (unique), timezone,
created date.

**`customers.Customer`** belongs to a business and holds a name and phone number.

**`appointments.Service`** belongs to a business and describes something bookable: name,
duration in minutes, price.

**`appointments.Appointment`** joins a customer to a service at a start time, with a
status of pending, confirmed, cancelled or completed. Defaults to pending.

**`reminders.Reminder`** belongs to an appointment, with the time the reminder should go
out and a flag for whether it has been sent.

Deleting a business cascades to its customers and services, which cascades to their
appointments, which cascades to their reminders.

## Licence

Proprietary. All rights reserved. See [LICENSE](LICENSE).

The code is public so it can be viewed, but it is not licensed for reuse, modification
or redistribution. Forking is possible on any public GitHub repo and is not a licence
grant.

## Contact

William

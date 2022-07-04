# Music Venue API v2 (Django)

Refactored API using Django instead of Flask. Tools and external libraries include Django and Django Rest Framework - powered by a SQL database consisting of over 1300+ music and sports venues. The api can be quered to retrieve the venue name, capacity, city, state, etc. or to add new venues.

### Development Setup

1. `virtualenv venv`
1. `source venv/bin/activate` or `source venv/Scripts/activate`
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. `python manage.py runserver`

### Endpoints

1. `/venues`
    - `GET, POST, PUT, PATCH, DELETE`

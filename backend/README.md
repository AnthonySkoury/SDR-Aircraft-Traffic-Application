# Air-Traffic System Backend

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.1.2-brightgreen.svg)](https://djangoproject.com)

## Django REST Tutorials

* [Part 1 - Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
* [Part 2 - Serialization](https://www.django-rest-framework.org/tutorial/1-serialization/)
* [Part 3 - Requests and Responses](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)
* [Part 4 - Class-based Views](https://www.django-rest-framework.org/tutorial/3-class-based-views/)
* [Part 5 - Authentication & Permissions](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)
* [Part 6 - Relationships & Hyperlinked APIs](https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/)
* [Part 7 - ViewSets & Routers](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)

For more info on the Django REST framework [click here](https://www.django-rest-framework.org).

For more info on the Django [click here](https://www.djangoproject.com/).

## Running the backend

Clone the repository to your local machine:

```bash
git clone https://github.com/AnthonySkoury/Air-Traffic-System.git
```

Get set up with the virtual environment for dependencies:
```bash
pip install pipenv
pipenv shell
```

Install the requirements from the Pipfile:

```bash
pipenv sync
```

Create the database:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Backend located at **127.0.0.1:8000** or http://localhost:8000 .

## Notable Backend Files

* [models.py](https://github.com/AnthonySkoury/Air-Traffic-System/blob/main/backend/aircraft/models.py) Database Tables defined in Django Models
* [serializers.py](https://github.com/AnthonySkoury/Air-Traffic-System/blob/main/backend/aircraft/serializers.py) Serializers used to convert the SQL data into JSON or JSON into SQL
* [api.py](https://github.com/AnthonySkoury/Air-Traffic-System/blob/main/backend/aircraft/api.py) API for viewsets which are used as the interface between the users with the data models/tables
* [urls.py](https://github.com/AnthonySkoury/Air-Traffic-System/blob/main/backend/aircraft/urls.py) Defined URLs for API
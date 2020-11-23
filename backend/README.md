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

## Database

### Setup
To work with the Django backend, first a PostgreSQL database is required. The recommended approach would be to use a PostgreSQL Docker Container.

Docker can be set up on the Raspberry Pi or on another machine.

[To install on Raspberry Pi](https://docs.docker.com/engine/install/debian/)

[To install on Mac/Windows/Linux PC](https://docs.docker.com/get-docker/)

To run a PostgreSQL Container in Docker, the image needs to be installed.

[PostgreSQL Image](https://hub.docker.com/_/postgres)

The following command can be used to set up the Docker Container. Note that the password can be changed but the name and port should stay consistent as they are the expected ones in the Django database settings. Django will use those to connect to the database.

```bash
docker run --name aircraft_db -e POSTGRES_USER=aircraft_db -e POSTGRES_DB=aircraft_db -e POSTGRES_PASSWORD=raspberry -d -p 5432:5432 postgres
```
### Backups

Since the database is separate from Django, it can be backed up/dumped through PostgreSQL pg_dump wherever it is hosted. If it is hosted in a Docker container, the following command can be used to dump the database into a SQL file. Note that it zips the file to save space and also appends a timestamp.

```bash
docker exec -t aircraft_db pg_dumpall -c -U aircraft_db | gzip > dump_$(date +"%Y-%m-%d_%H_%M_%S").gz
```
The following command can be used to unzip the dump file (must use generated timestamp).

```bash
gunzip dump_timestamp.gz
```

To load the database in Docker the following command can be used after unzipping the backup.

```bash
cat dump_unzipped_file | docker exec -i aircraft_db psql -U aircraft_db -d aircraft_db
```

Alternatively, the database can be dumped into JSON format via the manage functions provided by Django. The following command will dump it into a nicely formatted json file.

```bash
python manage.py dumpdata aircraft --indent=4 --natural-foreign --natural-primary > data.json
```

### PostgreSQL interface

To start the database Docker container in bash the following command can be used.

```bash
docker exec -it aircraft_db bash
```

To start psql to execute SQL statements and queries, the following command can be used.

```bash
docker exec -it aircraft_db psql -U aircraft_db -d aircraft_db
```


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
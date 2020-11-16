# erms

The following application is init and run in local env on Linux OS!!!

**Requirements:**

 - OS: Linux
 - Python 3
 - pip3
 - Django
 - PostgreSQL


**Installation steps:**

 - virtualenv venv
 - source venv/bin/activate
 - pip3 install -r requirements.txt
 - sudo su - postgres
 - psql
 - CREATE DATABASE erms;
 - GRANT ALL PRIVILEGES ON DATABASE erms TO root;
 - python3 manage.py makemigrations
 - python3 manage.py migrate
 - python3 manage.py createsuperuser


**Run application:**

- sudo ./run.sh


**Important:**

The records for Department and Job Position models can be created from admin panel: "/admin".
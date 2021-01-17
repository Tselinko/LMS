# LMS
My LMS for PPPoSD'20 Tinkoff

Requires Python 3.6

Rest of the requirements should be installable with pip.

Uses Postgres by default. As of now there isn't anything Postgres specific in the codebase so it should be portable to Mysql just by flipping the database engine.

# Installation
- Create a project directory
mkdir django-lms

cd lms

- Create a virtual environment.
virtualenv venv

- Activate the environment
source venv/bin/activate

- clone the repo
git clone https://github.com/Tselinko/LMS.git

- Use the requirements file in the repo
pip install -r lms/requirements.txt

- Run to start project

  python3 manage.py makemigrations

  python3 manage.py migrate

  python manage.py runserver

The application is now installed. 

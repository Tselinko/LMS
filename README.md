# LMS
My LMS for PPPoSD'20 Tinkoff

Requires Python 3.6

Rest of the requirements should be installable with pip.

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
  
  cd LMS/WebApp/LMS

  python3 manage.py makemigrations

  python3 manage.py migrate

  python manage.py runserver

The application is now installed. 

# Demo testing

21 profiles are already created:

- from A@gmail.com to AAAAAAAAAA.@gmail.com and from C@gmail.com to CCCCC@gmail.com - students

- from B@gmail.com to BBBBB.@gmail.com - teachers

- admin@gmail.com - superuser

All profiles have the same password: Tsel2506

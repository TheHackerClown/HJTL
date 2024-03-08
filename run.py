from os import system as sys

sys('pip install -r requirements.txt')
sys('python manage.py collectstatic')
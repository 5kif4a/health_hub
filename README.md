```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd health_hub
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8080
```

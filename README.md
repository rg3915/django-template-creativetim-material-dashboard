# django-template-creativetim-material-dashboard

This template is free and based on [Material Dashboard 2](https://github.com/creativetimofficial/material-dashboard/) by [Creative Tim](https://www.creative-tim.com/product/material-dashboard).

## This project was done with:

* [Django 4.2.1](https://www.djangoproject.com/)
* [Material Dashboard 2 template](https://github.com/creativetimofficial/material-dashboard/)

### Libs Python

* [django-extensions](https://django-extensions.readthedocs.io/en/latest/)
* [python-decouple](https://pypi.org/project/python-decouple/)
* [djhtml](https://pypi.org/project/djhtml/0.0.3/)

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/django-template-creativetim-material-dashboard.git
cd django-template-creativetim-material-dashboard

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```


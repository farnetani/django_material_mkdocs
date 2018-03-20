# django_material_mkdocs

Template Material para Mkdocs com Senha através do Django (django-allauth)

Simplesmente une 2 projetos: django_mkdocs + mkdocs-material

Arlei F. Farnetani Junior
farnetani@gmail.com


# DEMO
https://farnetani.github.io/estudos/

https://farnetani.github.io/estudos/Django/00.%20Agradecimentos/

**Instalação:**

* Requer python version `3.4` or `3.5` ou superior
* `mkdir myproject`
* `cd myproject`
* `python -m venv .venv`
* `WINDOWS: .venv\Scripts\activate`
* `pip install -r requirements.txt` in a proper venv
* `mkdocs build`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* `python manage.py runserver`
* Open `http://localhost:8000/docs/`
* Login with the created superuser.
* Já era, só ser feliz!

**Requirements**

```
Django==2.0.3
PyYAML==3.12
django-allauth==0.35.0
mkdocs>=0.17.1
Pygments>=2.2
pymdown-extensions>=3.4
```

## django_mkdocs

`https://github.com/HackSoftware/django_mkdocs`

`https://www.hacksoft.io/blog/integrating-a-password-protected-mkdocs-in-django/`

## Tema Material

`https://squidfunk.github.io/mkdocs-material/`

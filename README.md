# django-fullstack

django-fullstack
"We have several projects that use a django-fullstack, which is very impressive and makes it easy for us to connect the frontend and backend. Next, we want to make our django-fullstack usable by many other frontend frameworks or create one that can be chosen among them. We are also continuously developing all our projects well and consistently asking our team to look for any flaws in our django-fullstack."


- **Flexsibel**
- **easy to build**
- **support django 5.0**
- **django friendly**
- **Fast To code**

### requirement
- python >= 3.9 < 3.13
- django >= 3.0 < 6.0
- django-fullstack >= 0.1.0 < 2.0.0

##how to install django-fullstack

#install using pip
```
pip install django-fullstack
```
#install using poetry
```
poetry add django-fullstack
```

```python
INSTALLED_APPS = [
    ...'
    'django-fullstack',
]
```

```python
 # For Setting Django Fullstack
    DJANGO_FULLSTACK = {
        "RENDER": {
            "INDEX": "index.html",
            "URL_SSR": "http://localhost:13714",
            "ENABLED_SSR": False,
        },
        "TEMPLATE": {
            "DEV_MODE": getattr(django_settings, "DEBUG", True), # false to production
            "SERVER_PROTOCOL": "http",
            "DEV_SERVER_HOST": "localhost",
            "DEV_SERVER_PORT": 5173,
            "WS_CLIENT_URL": "@vite/client",
            "ASSETS_PATH": Path(getattr(django_settings, "STATIC_PATH", "static"))
            / "dist",
            "STATIC_URL_PREFIX": "",
            "LEGACY_POLYFILLS_MOTIF": "legacy-polyfills",
        },
        "STATIC_ROOT": "static",
        "CSRF_HEADER_NAME": "HTTP_X_XSRF_TOKEN",
        "CSRF_COOKIE_NAME": "XSRF-TOKEN",
    }
```

# run django

*using python*
```
python manage.py runserver
```

*using pypy3*
```python
pypy3 -m manage.py runserver
```

#run frontend
```
npm run dev
```


"To run the backend and frontend simultaneously, you need to run both by opening two terminals, one for Django and the other for the frontend. Once they are running, you can open your browser using http://localhost:8000 or http://127.0.0.1:8000."

thank you for
django-breeze
django-vite
inertia-django

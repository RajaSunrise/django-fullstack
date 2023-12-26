# django-fullstack

#### INTRODUCTION PROJECT
We have several projects that use a django-fullstack, which is very impressive and makes it easy for us to connect the frontend and backend. Next, we want to make our django-fullstack usable by many other frontend frameworks or create one that can be chosen among them. We are also continuously developing all our projects well and consistently asking our team to look for any flaws in our django-fullstack.


- **Flexsibel** : flexsibel to coding and easy 
- **easy to build** : easy to build frontend & backend
- **support django 5.0** : support django 5.0 and async django
- **django friendly** : you can integration django and frontend
- **Fast To code** : simple code and create new project fast

### requirement
- python >= 3.9 < 3.13
- django >= 3.0 < 6.0
- django-fullstack >= 0.1.0 < 2.0.0

### documentation
- [introduction](#introduction-project)
  - [installation](#how-to-install-django-fullstack)
  - [create project](#how-to-create-project-django-fullstack)
  - [setup django-fullstack](#setup-to-settingpy)
  - [create frontend](#make-your-app-react-or-vue)
  - [install frontend](#install-frontend)
  - [run server](#run-you-server)
  - [staticfiles](#staticfiles)
  - [project to production](#production-your-project)
- [THANKS FOR SUPPORT](#thanks-you-for-support)

### how to install django-fullstack
-------------------------------
**1. install using pip**
```
pip install django-fullstack
```
**or install using poetry**
```
poetry add django-fullstack
```

how to create project django-fullstack
-------------------------------------
command using django-fullstack
```bash
django-fullstack startproject name-project
```
command using django
```bash
django-admin startproject name-project
```

setup to setting.py
------------------

Add to ```setting.py``` on your project
```python
INSTALLED_APPS = [
    ...'
    'django_fullstack',
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
            "SERVER_PROTOCOL": "http",
            "DEV_SERVER_HOST": "localhost",
            "DEV_SERVER_PORT": 5173,
            "WS_CLIENT_URL": "@vite/client",
            "ASSETS_PATH": "static/dist",
            "STATIC_URL_PREFIX": "", # add if you prefix your url stactic
        },
        "STATIC_ROOT": "static",
        "CSRF_HEADER_NAME": "HTTP_X_XSRF_TOKEN",
        "CSRF_COOKIE_NAME": "XSRF-TOKEN",
    }
```

make your app react or vue
--------------------------
generate your file react or vue

```bash
django-fullstack create-app vue #use --typescript for using typescript
```

```bash
django-fullstack create-app react #use --typescript for using typescript
```

### Install frontend
this command to install package frontend
support ```nodejs v16 - v20``` and ```npm > v9```

```bash 
npm install 
#or 
yarn install
#or
pnpm install
```

run you server
----------

To run the backend and frontend simultaneously, you need to run both by opening two terminals, one for Django and the other for the frontend. Once they are running, you can open your browser using http://localhost:8000 or http://127.0.0.1:8000.
*1. using python*
```
python manage.py runserver
```

*or using pypy3*
```python
pypy3 -m manage.py runserver
```

*run frontend*
```
npm run dev
```
**visit your host django http://localhost:8000 or http://127.0.0.1:8000**

staticfiles
------------
if you want to display image or other file in a non-conventional way react and vue, the use folowing :

**Image and other file**
```html
<img className="w-full lg:w-[60%]" src="/static/image/image.jpg" alt="bla bla"
    />
```
Production your project
----------------------
1. build your frontend
```bash
npm run build
#or
yarn run build
#or
pnpm run build
```
2. debug your django in ```setting.py```
```python
DEBUG = False
```
3. make your project to collectstatic
```bash
python manage.py collectstaic
#or
pypy -m manage.py collectstatic
```

### thanks you for support
---------------------
- *<a href="https://narmadaweb.com">NARMADAWEB</a>*
- *<a href="https://itec.sch.id"> ITEC </a>*
- *DJANGO INDONESIA & TEAM*

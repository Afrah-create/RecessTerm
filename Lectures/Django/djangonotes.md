# Introduction to Django

Django is a high-level Python web framework that enables rapid development and clean design. 

## The MVT Architecture

Django uses the Model-View-Template (MVT)** architecture to separate data management, business logic, and the user interface.

### Purpose
* Separation of concerns: Keeps data, logic, and presentation completely independent.
* Maintainability: Makes codebases highly organized and easy to scale.

### Structure
* Model: Manages data structure and database communication.
* View: Handles business logic and processes user requests.
* Template: Renders the visual HTML layout for users.

## Creating a New Project

### Step 1: Install Django
```bash
pip install django
```

### Step 2: Initialize Project
```bash
django-admin startproject myproject
```

### Step 3: Enter Directory
```bash
cd myproject
```

### Step 4: Start Server
```bash
python manage.py runserver
```

### Step 5: Verify Setup
* Open browser.
* Go to `http://127.0.0`.

### Purpose of Each File in a New Django Project

When you run `django-admin startproject myproject`, Django generates a specific root directory structure. Here is the purpose of every file created:

* `manage.py`: A command-line utility that lets you interact with your Django project. You use it to run the server, create migrations, and manage databases.
* `myproject/` (Inner Folder): This is the actual Python package for your project. Its name is used to import files.
* `__init__.py`: An empty file that tells Python this directory should be treated as a Python package.
* `settings.py`: The main configuration file for your project. It contains database settings, registered apps, security keys, middleware, and static asset routes.
* `urls.py`: The routing configuration and "table of contents" for your project. It maps URL paths to views.
* `asgi.py`: Entry point for ASGI-compatible web servers. It is used to deploy your project on asynchronous servers for features like WebSockets.
* `wsgi.py`: Entry point for WSGI-compatible web servers. It is the standard configuration used to deploy your project to traditional synchronous production servers.


### Where to Create Models, Views, and Templates

You do not create models, views, or templates inside the core project folder. Instead, Django uses a modular system called **Apps**. You must create a Django app inside your project to hold these components.

Run this command in your terminal to create an app:
```bash
python manage.py startapp myapp
```

This creates a new folder named `myapp` with its own structure:
* **`models.py`**: Create your data models here.
* **`views.py`**: Write your business logic and request handlers here.
* **`templates/`**: Create this folder manually inside `myapp` to hold your HTML files.

---

### Step-by-Step Interconnection Guide

Here is how to interconnect all the components, one file at a time, to make a working web page.

#### Step 1: Register the App in `settings.py`
Django needs to know your new app exists so it can find its models and templates.
* Open `myproject/settings.py`.
* Add your app name to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    # Default Django apps...
    'myapp', 
]
```

#### Step 2: Define Data in `myapp/models.py`
Define the structure of the data you want to store.
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
```
*After writing a model, you run `python manage.py makemigrations` and `python manage.py migrate` using **`manage.py`** to sync this model to your database.*

#### Step 3: Fetch Data and Handle Logic in `myapp/views.py`
The view acts as the middleman. It pulls data from the model and sends it to the template.
```python
from django.shortcuts import render
from .models import Item

def item_list(request):
    # Fetch all items from the Model database
    items = Item.objects.all() 
    # Pass the data to the Template
    return render(request, 'myapp/items.html', {'items': items})
```

#### Step 4: Display Data in `myapp/templates/myapp/items.html`
Create the HTML layout to display the data sent by the view.
```html
<!DOCTYPE html>
<html>
<head><title>Item List</title></head>
<body>
    <h1>Our Items</h1>
    <ul>
        {% for item in items %}
            <li>{{ item.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### Step 5: Route the URL in `myproject/urls.py`
Finally, map a web address to your view so users can visit the page.

```python
from django.contrib import admin
from django.urls import path
from myapp import views # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', views.item_list, name='item-list'), # Map URL to the view
]
```

myproject/                  <-- Root folder (project container)
│
├── manage.py               <-- Terminal tool (never edit this file)
│
├── myproject/              <-- Core Project Folder (the "wrapper")
│   ├── __init__.py         <-- Blank file (tells Python this is a package)
│   ├── asgi.py             <-- For async deployment (leave alone)
│   ├── settings.py         <-- Settings (you add 'myapp' to INSTALLED_APPS here)
│   ├── urls.py             <-- Root routing (you link myapp's URLs here)
│   └── wsgi.py             <-- For standard deployment (leave alone)
│
└── myapp/                  <-- Your App Folder (where 90% of your work happens)
    ├── __init__.py         <-- Blank file
    ├── admin.py            <-- Register models here to see them in admin panel
    ├── apps.py             <-- App configuration details (leave alone)
    ├── models.py           <-- Create database tables here
    ├── tests.py            <-- Write test code here
    ├── views.py            <-- Write backend logic and functions here
    │
    ├── migrations/         <-- Automatically tracks database changes (don't touch)
    │   └── __init__.py
    │
    └── templates/          <-- Folder you manually create inside the app
        └── myapp/          <-- Subfolder with app name (best practice)
            └── index.html  <-- Your actual frontend HTML files




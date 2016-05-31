Django is a free and open source web application framework written in Python.

Virtual Environment:
    Isolates Python/Django set up on a per-object basis, so changes to one website won't affect others that you're developing. 
    $ python3 -m venv myvenv(arbiturary)  <!--creates a virtualenv -->
    $ source myvenv/bin/activate <!-- start virtual environment -->
    <!-- console will be prefixed with (myvenv) when it's activated -->
Installing Django:
    (myvenv) ~$ pip install django~=1.9.0


Getting started:
    (myvenv) ~$ django-admin startproject mysite(arbitrary) .

<!-- the . tells the script to intall Django in your current directory -->
    Creates manage.py and a mysite directory. 
    manage.py is a script that helps with management of the site. Able to start a web server on our computer without installing anything else.
    settings.py contains the configurations of your site. 
    urls.py contains a list of patterns used by urlresolver

Database is a collection of data, where a model gets saved. 
To setup a database goto mysite/settings.py, under DATABASES. Default set to sqlite3.
In the terminal goto the directory that contains manage.py file, then type: 
    python manage.py migrate <!-- creates a database -->
Start the web server: python manage.py runserver

To create an application:
    (myvenv) $python manage.py startapp blog(name)

Goto mysite/settings.py, under INTALLED_APPS, add 'blog', (include comma) to tell django to use the application. 


Models get defined in blog/models.py


Defining a model:
    class Post(model.Model)
Define properties of the model. Ex: title = models.CharField(max_length=100)
text = models.TextField()


python manage.py makemigrations blog 
<!-- adds the new model to the database -->

python manage.py migrate blog
<!-- applies the migration file to the database -->


In blog/admin.py:
    from django.contrib import admin
    from .models import Post<!-- import the Post model -->

    admin.site.register(Post) <!-- makes the model visible on the admin page --> 

python manage.py createsuperuser <!-- creates a superuser -->

URLs in Django
urlpatterns = [
    url(r'^) <!-- uses regex to match URLs to views -->
]


blog/views.py  <!-- where we request information from the model we created before and pass it to a template -->

Querysets - list of objects of a given Model. Allows you to read the data from the database, filter it and order it. 

python manage.py shell <!-- Django's interactive console -->

from blog.models import Post <!-- import Post -->

Post.objects.all()

Post.objects.create(author=me, title=, etc..)

Post.objects.filter(condition)

Post.objects.get(condition)





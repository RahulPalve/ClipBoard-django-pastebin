# ClipBoard-django-pastebin

This is ClipBoard.

A Django 2.0 powered web application which is text storage web app follows paste and share model. 

Similar and alternative to Pastebin, tinypaste, hastebin etc.

# Getting Started
To setup this project, create a virtual environment using Python 3.6 or higher and run the following command in your terminal (ensure that you are in the project directory):

~~~ 
$ pip install -r requirements.txt 
~~~
It will set your environment up to run the project

Run the following commands in your terminal:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
This will set your SQL database up and run your local server. Press ```ctrl+c to``` stop the server.

You will find a directory named ```todoapp ``` in the root directory of the project, most of your code should go there.

Do remember to run ```python manage.py makemigrations``` in your terminal before committing changes.


# Some of screenshots:

Index Page:


![alt text](https://github.com/RahulPalve/ClipBoard-django-pastebin/blob/master/todoapp/static/images/index.png)


Paste Details:


![alt text](https://github.com/RahulPalve/ClipBoard-django-pastebin/blob/master/todoapp/static/images/detailed.png)

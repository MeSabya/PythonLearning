## Flask Blueprints
The commonly accepted pattern for large projects is to break your project into multiple packages using Flask Blueprints.

A **blueprint** is a package that encapsulates one specific piece of functionality in your application. 
You should think of a flask application structured using blueprints as several key pieces of functionality working together to deliver the complete web application.

Before you start coding your project, it is a good idea to first give thought to what blueprints you can divide the application into. My personal approach is to use two blueprints, auth and main. The auth blueprint handles all the functionality related to users- registration, login, logout, password reset and account confirmation. The main blueprint handles the functionality and features unique to the application. You could also add a third blueprint, api, for handling programmatic access to the web application resources.

You should create the following project structure for a project with two blueprints:

|-application.py
|-config.py
|-.env
|-.gitignore
|-readme.md
|-requirements.txt
|-celery_worker.py
|-Dockerfile
|-docker-compose.yml
|-pytest.ini
|-env/
|-tests/
    |-conftest.py
    |-test_main.py
    |-test_auth.py
    |-test_models.py
|-app/
    |-__init__.py
    |-models.py
    |-forms.py
    |-tasks.py
    |-static/
    |-templates/
        |-base.html
        |-400.html
        |-403.html
        |-404.html
        |-405.html
        |-500.html
    |-auth/
        |-__init__.py
        |-views.py
        |-forms.py
        |-templates/auth
            |-register.html
    |-main/
        |-__init__.py
        |-views.py
        |-forms.py
        |-templates/mai
            |-index.html

👉 When you use blueprints, the view functions that handle requests won’t all be in one file; they are going to be split across different files. 
Each blueprint will have its own views.py file containing the code belonging to it. 
Instead of the routes having an **@app decorator**, they will be decorated with the name of the blueprint they belong to eg **@auth_blueprint.route('/login')**

👉 Once you have organised your project into blueprints, instead of the server passing requests to the flask application instance to be handled, 
the requests are pushed to the appropriate blueprint and the blueprint handles them. 
For the flask application instance to know the blueprints in the project and the routes that belong to it, the blueprints have to “register” with the flask application instance.

### Define Your Blueprints
Each blueprint must have an __init__.py file. In this file, you define the blueprint by instantiating an instance of the Blueprint class. 

👉 The arguments passed to the class constructor are the name of the blueprint and the name of the folder containing the templates belonging to the blueprint. 
You then need to import the routes associated with that blueprint, that are written in the views.py located in the same directory as the __init__.py module.

###### In app/auth/__init__.py:

```python
from flask import Blueprint

main_blueprint = Blueprint('auth', __name__, template_folder='templates')

from . import views
```
###### In app/main/__init__.py:

```python
from flask import Blueprint

main_blueprint = Blueprint('main', __name__, template_folder='templates')

from . import views
```

***When working with blueprints:***

- Make sure that the decorator used to define any route uses the blueprint object.
- Make sure that the render_template() function argument takes the form blueprint_name/template_name.html . This is done to reflect the fact that a blueprint can only render templates that belong to it.
- Make sure that the url_for() function references the blueprint associated with the view function. This is done to reflect the fact that view functions belong to specific blueprints. url_for(auth.login).
- Any reference you would make to the app object needs to be replaced by the current_app object. This is because when you are working with blueprints, you no longer have access to the flask application instance directly. You can only get access to it via its proxy, current_app.
- If you specified a prefix for a blueprint in the blueprint registration, the route in the view function decorator doesn’t get that prefix (that is, the decorator is not @auth_blueprint.route('/users/login') as you would have thought). However, a request recieved for that route from a client must contain the prefix otherwise the server will return a 404 error.
- In the blueprint’s directory, you need to create a templates folder, and then inside that templates folder another folder named after the blueprint. The templates associated with the blueprint are stored in the directory with the name of the blueprint. This approach is the advised way of storing templates associated with the view functions of a blueprint.


###### In app/auth/views.py:

```python
from . import main_blueprint
from flask import render_template, request, redirect, url_for

@main_blueprint.route('/')
def index():
    return render_template('main/index.html')
```   

###### In app/auth/templates/auth/register.html:

<h1>Hello world from the auth blueprint!</h1>

###### In app/main/views.py:
```python
from . import main_blueprint
from flask import render_template, request, redirect, url_for

@main_blueprint.route('/')
def index():
    return render_template('main/index.html')
```

###### In app/main/templates/main/index.html:
<h1>Hello world from the main blueprint!</h1>







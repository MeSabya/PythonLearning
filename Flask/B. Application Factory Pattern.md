## Application Factory Pattern

Typically, a flask application is instantiated with a global scope. What this means is that when you run the flask application script, the flask app gets instantiated and configured right away. And unfortunately, once it is running, there is no way to change its configuration settings.

This is not ideal behavior. You want to be able to create different versions of the same flask application that are configured for different environments (development, testing or production).

A solution is to move the instantiation and configuration of the flask application into a function. 
The approach of using an application factory function and then calling it when you want to create a flask application instance is actually 
a well-known design pattern referred to as the **Factory Method Pattern.**




An HTTP load balancer is an HTTP proxy server that handles HTTP requests on behalf of other servers. This is what we'll be developing throughout this course. To assist in that effort, we'll be using the following tools:

- Flask is a popular Python web framework.
- pytest is a testing framework.
- venv is used for creating isolated Python environments.
- Make is an automation tool that generates executable and non-source files
- Docker is a containerization tool designed to simplify the development and deployment of applications.
- Docker Compose is to run multiple instances of a Backend.

## Commands

```shell

$ mkdir http-load-balancer
$ cd http-load-balancer
$ python3.9 -m venv env
$ source env/bin/activate

(env)$ python -V
Python 3.9.0

(env)$ pip install flask pytest

```
Load Balancer functional requirements:
======================================
- Since we are testing a load balancer functionality , we are going to spawn the application instances using docker compose yaml file.
- Then we should add functionality to add configuration files to add hardcoded host names and ip addresses.
- Load balancer should able to check health check of servers.
- Load balancer should able add firewall functionality.
- It should able to Manipulate the HTTP Request. 

#### Why Manipulate the HTTP Request?
HTTP requests are made up of different parts like headers, cookies, parameters, and data, to name a few. You may want to do different things based on the values of those parts.

**Examples:**

👉 You may want to configure your load balancer to send the client to a mobile-friendly version of your website. To do so, you can inspect the User-Agent header, determine if it's from an Android or iPhone browser, and then send it to the appropriate set of servers whilst adding additional headers.

👉 Another possible use case is to serve up localized versions of a site based on the Accept-Language header.

**We are trying to understand the https://testdriven.io/courses/http-load-balancer/routing/#H-5-multiple-backends**

```yaml
version: '3'
services:
  mango1:
    image: server
    environment:
      - APP=mango
    ports:
      - "8081:5000"
  mango2:
    image: server
    environment:
      - APP=mango
    ports:
      - "8082:5000"
  apple1:
    image: server
    environment:
      - APP=apple
    ports:
      - "9081:5000"
  apple2:
    image: server
    environment:
      - APP=apple
    ports:
      - "9082:5000"
 ```
 
 If we observe carefully all containers are running on container port 5000 and host port is different. 
 [How to Use Docker Compose to Run Multiple Instances of a Service in Development](https://pspdfkit.com/blog/2018/how-to-use-docker-compose-to-run-multiple-instances-of-a-service-in-development/)
 
 
 

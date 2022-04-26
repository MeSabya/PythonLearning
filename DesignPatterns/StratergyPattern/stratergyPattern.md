# Strategy pattern

*The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. 
Strategy lets the algorithm vary independently from clients that use it.*


To understand the strategy design pattern, let's take an example of a transport system. You are developing an application, 
which provides the time estimation for user-selected routes. There are different kinds of transports available like public transport, 
car, and bike. Each mood of transport has different estimation times based on their speed and other factors.

The simple approach to solve it is using the if…else conditions. Each transport mood will be available in a different ‘if ’block of code. 
This approach will lead to problems while maintaining the code in the long run. Each time we need to add new functionality, code modification will be required.
The better approach to implement it is by using the strategy design pattern.

```python
class Transportation:
    def calculate_time(self, transportation_type):
        if transportation_type == 'CAR':
            pass
        elif transportation_type == 'PUBLIC':
            pass
        elif transportation_type == 'BIKE':
            pass
```

The problem would be :

1. What if we need to add another transportation_type . 
2. What if we need to add another method.

Solution to the above is Strategy pattern.

![image](https://user-images.githubusercontent.com/33947539/165215038-dbbbf641-0354-4faf-a94f-a720d462a22d.png)

```python
from abc import ABC, abstractmethod
import datetime

class Transport(ABC):
    @abstractmethod
    def compute_time(self, distance):
        pass

class PublicTransport(Transport):
    def compute_time(self, distance):
        self.speed = 15
        estimated_hours = distance / self.speed
        return str(datetime.timedelta(hours=estimated_hours))

class CarTransport(Transport):
    def compute_time(self, distance):
        self.speed = 30
        estimated_hours = distance / self.speed
        return str(datetime.timedelta(hours=estimated_hours))

class BikeTransport(Transport):
    def compute_time(self, distance):
        self.speed = 50
        estimated_hours = distance / self.speed
        return str(datetime.timedelta(hours=estimated_hours))

class RouteSelection:
    def __init__(self, transport_type):
        self.transport = transport_type
    
    def time_estimation(self, distance):
        return self.transport.compute_time(distance)

if __name__ == '__main__':

    public_transport = PublicTransport()
    route_selection = RouteSelection(public_transport)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))

    car = CarTransport()
    route_selection = RouteSelection(car)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))

    bike = BikeTransport()
    route_selection = RouteSelection(bike)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))
    
 ```   

## Another Example:

Let’s say you are tasked to monitor a mission-critical system that is highly available, resilient and fault-tolerant. To ensure that the production system meets its objectives, it is essential to send alerts to the developers, on-call Site Reliability Engineers and other stakeholders. The monitoring & alerting system would have different rules configured such as sending an email alert when error logs cross a threshold, a slack notification when a service goes down or SMS notification to on-call person.

This can also be done using if/else statements.

In future, multiple requirements might spring up. A few of the requirements that strike my mind are as follows:-

1. Use an alternative messaging platform to slack
2. Record all the alerts in a database or a file
3. Send alerts to a different service in the cluster via an API call
4. Modify the template used to send the email

Solution to the above: strategy design pattern

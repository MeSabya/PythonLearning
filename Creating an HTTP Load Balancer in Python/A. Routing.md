## Why Do We Need Routing?
Routing is a general concept in networking which refers to the path a packet takes to reach a destination. 
In our case, when we implement routing in a load balancer we're referring to how HTTP requests reach other collections of servers (or different backend servers).
Different routing strategies can be used to control the behavior of the load balancer.

## What's Host-based Routing?
With host-based routing, requests are directed based on the request host header. 
If the header is not found then the load balancer returns a 404 to the client.

![image](https://user-images.githubusercontent.com/33947539/190897713-bcdd66fc-65ab-43b4-bf85-c85a19bcd089.png)

In the above example, the client on the left sends their host header as "www.mango.com" and the load balancer directs them to the mango backend servers. The client on the right, meanwhile, sends "www.notmango.com" and gets a "404 Not Found" back because the load balancer only recognizes "www.mango.com" and "www.apple.com".

## What's Path-based Routing?
👉 **Path-based routing relies on the URI to send the request to the backend servers.**

#### For example:

```
https://www.mywebsite.com/apples
https://www.mywebsite.com/mangoes
```

Let's break down the above:

https is the protocol
www.mywebsite.com is the fully qualified domain name (FQDN)
/apples and /mangoes are the paths
If someone requests the /apples path, we'll direct the request to the apples backend servers and if someone hits the /mangoes path we'll direct them to the mangoes backend server.

Path-based routing is a very common pattern for creating microservices to break a large web application into a smaller one. 
As with the above example, host-based and path-based routing complement each other: Essentially, path-based routing relies on host-based routing.




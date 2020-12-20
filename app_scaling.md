* This document describes steps in which this app can be scaled
* The focus of this document will be on scaling the app horizontally

#### First Step
* The first simplest way to scale is to deploy the exact same codebase 
to multiple application servers and put a load balancer in front of it 
* Sessions (if needed) will be stored in a centralized data store which is accessible to all application servers. 
This can be done with something like Redis
* The first step will enable to serve thousands of concurrent requests

#### Second Step
* The second step will be to denormalize data
* All the joins should be done in the application code itself instead of the database queries

#### Third Step
* Soon the database will again become the bottleneck
* The third step will now be to introduce a cache between the application servers and the database
* Redis can be used for this purpose
* There are two patterns in which can be used:

1. Cached Database Queries:
⋅⋅* The query can be hashed and the result of it can be stored as value

2. Cached Objects with Asynchronous processing:
..* In this a complete instance of a class (object) is stored in the cache 
after initially fetching from the database.
Example: A user profile is loaded each time a user logs in.
This whole user object can be stored in the cache.
..* The above caching of the objects can be done asynchronously in the 
background using many workers (servers, processes and threads) to make 
this more efficient

#### Fourth Step
* Replicas of the Database can be created so that reads are directed towards the Replicas 
and the master can handle the writes. This will further improve the number of requests handled by the system

#### Additional Optimizations
* Separate workers can asynchronously do the book rental calculations and keep them ready.
This way the user can quickly see the total charges


## Scaling the app
* This document describes steps in which this app can be scaled
* The focus of this document will be on scaling the app horizontally

#### First Step: Load Balancer and multiple servers
* The first simplest way to scale is to deploy the exact same codebase 
to multiple application servers and put a load balancer in front of it 
* Sessions (if needed) will be stored in a centralized data store which is accessible to all application servers. 
This can be done with something like Redis
* The first step will enable to serve thousands of concurrent requests

#### Second Step: Denormalize data
* The second step will be to denormalize data
* All the joins can be done in the application code itself instead of the database queries
* This will help in scaling the application

#### Third Step: Add Caching mechanism
* Soon the database will again become the bottleneck
* The third step will now be to introduce a cache between the application servers and the database
* Redis can be used for this purpose
* There are two patterns which can be used in this:

1. Cached Database Queries:
⋅⋅* The db query can be hashed and the result of it can be stored as value

2. Cached Objects with Asynchronous processing:

* In this a complete instance of a class (object) is stored in the cache 
after initially fetching from the database.
Example: A user profile is loaded each time a user logs in.
This whole user object can be stored in the cache.

* The above caching of the objects can be done asynchronously in the 
background using many workers (servers, processes and threads) to make 
this more efficient

#### Fourth Step: Adding Replication
* Replicas of the Database can be created so that reads are directed towards the Replicas 
and the master can handle the writes. This will further improve the number of requests handled by the system

#### Additional Optimizations
* Separate workers can be created which asynchronously do the book rental calculations and keep them ready.
This way the user can quickly see the total charges quickly when he logs in


## Deployment Steps using CI/CD with Circle CI
* Create an account on https://app.circleci.com/
* Connect the CircleCI app with the GitHub Repository
* Get the default config file from the Circle CI platform and use it as a starting point for the project
* Create a config.yml file in the .circleci folder in the root of the project
* Enable Google Cloud Registry on the GCP console
* Download the service account JSON file for the project from GCP console. This file is used for authentication.
* Add the above JSON file to the environment variables in the circleci app
* The config file is divided into two parts: One is for testing the code 
and other is for pushing the image to Google cloud
* Add the setup_remote_docker command so that docker containers can be remotely 
created on the circleci platform
* In the first part in the config, add instructions for installing docker-compose on the remote platform
* Next add commands so that tests can be run inside the docker container
* In the second part we add instructions for pushing the docker image to the Google Container Registry
* We use the value of the google_auth variable defined in the file for authentication. 
* The last command pushes everything to the Google Container Registry.
* In the last step we connect everything by adding dependency between the two parts
 

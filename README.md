# Platform for renting books and more
## Setup
* Pull the code from this git repository

* The containers can be started using the following command from the root directory of the project:
```
docker-compose up
```

* Tests can be run using the following command 
(Since this is running inside docker itself the previous command should have successfully run for this):
```
docker exec -it <name_of_django_container> /bin/sh -c "python manage.py test"
```
* Example:
```
docker exec -it goodreads-rental-master_django_1 /bin/sh -c "python manage.py test"
```



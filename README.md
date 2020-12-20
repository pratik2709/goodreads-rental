# Platform for renting books and more
## Setup
* Pull the code from this git repository

* The containers can be started using the following command from the root directory of the project:
```
docker-compose up
```

* Tests can be run using the following command:
```
docker exec -it goodreads-rental-master_django_1 /bin/sh -c "python manage.py test"
```



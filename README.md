# Platform for renting books and more
## Setup
* Pull the code from this git repository
* Create containers using this command in the root directory:
```
docker-compose build
```

* Once the containers are created, The containers can be started using the following command:
```
docker-compose up
```

* Tests can be run using the following command:
```
docker exec goodreads-rental_django_1 bash -c "python manage.py test"
```

Swagger can be accessed:
```
http://35.202.55.237/swagger/
```

Admin can be accessed:
```
http://35.202.55.237/admin/
```


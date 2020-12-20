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
docker exec -it goodreads-rental-master_django_1 /bin/sh -c "python manage.py test"
```

Admin can be accessed:
```
http://35.202.55.237/admin/
```

## Swagger
* Login into swagger using the following url:
```
http://35.202.55.237/swagger/
```



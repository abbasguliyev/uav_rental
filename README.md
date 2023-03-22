# uav_rental
UAV Rental Project with Django

## Project Demo
- Linux Server
- project demo : http://megaline.gq:9515
- Demo User Username: admin@example.com
- Demo User Password: admin123
- rest-api docs: http://megaline.gq:9515/docs/ ve http://megaline.gq:9515/redoc/

## Demo Screenshots
![Model](assets/Screenshot from 2023-03-23 00-42-40.png)

## Technologies and Libraries
1. Django
2. django-environ
3. django-filter
4. djangorestframework
5. djangorestframework-simplejwt
6. drf-yasg
7. Postgres
8. Docker and etc.

## Install
- git clone https://github.com/abbasguliyev/uav_rental.git
## Configuration
- create .env file inside src and uav_rental(for docker-compose) folders, copy and paste the contents of the uav_rental/env file.
## Run with Docker
- docker-compose build
- docker-compose run --rm web python3 manage.py createsuperuser
- docker-compose up

## Run without Docker
- cd kodaze
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
# uav_rental
UAV Rental Project with Django

## Project Demo
- Linux Server
- project demo : http://megaline.gq:9515
- Demo User Username: admin@example.com
- Demo User Password: admin123
- rest-api docs: http://megaline.gq:9515/docs/ ve http://megaline.gq:9515/redoc/

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

## Demo Screenshots
![<img alt="alt_text" width="10px" />](/src/media/assets/sc1.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc19.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc3.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc4.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc5.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc6.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc7.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc8.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc9.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc10.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc11.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc12.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc13.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc14.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc15.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc17.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc18.png?raw=true "Optional Title")
![<img alt="alt_text" width="10px" />](/src/media/assets/sc19.png?raw=true "Optional Title")

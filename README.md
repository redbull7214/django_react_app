<h1 align="center">Software accounting App</h1>

## Packages in this project
```
Django==4.2.4
django-redis==5.3.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
gunicorn==21.2.0
psycopg2-binary==2.9.7
PyJWT==2.8.0
redis==4.6.0

```
## Preparatory works
1. Setup [docker](https://docs.docker.com/get-docker/) and [docker compose v2](https://docs.docker.com/compose/cli-command/#installing-compose-v2);
2. Download the code:

```shell
https:
git clone https://github.com/redbull7214/django_react_app.git

ssh:
git clone git@github.com:redbull7214/django_react_app.git
```

3. Go to the project directory:
```shell
cd django_react_app
```
4. Create .env file.(optional)
Example:
```shell
API_TOKEN = 'your bot token from botfather'
```


## How to run the local version

Start the docker and enter django container:
```shell
docker compose up --build -d
docker-compose exec django sh
```
Run migrations, collect static and create superuser:
```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic 
```




## Urls
frontend
```
http://localhost:3000
```

django-admin
```
http://localhost/admin/
```
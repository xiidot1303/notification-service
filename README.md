# Notification service API

## Setup

Install the dependencies:
```sh
$ pip install -r requirements.txt
```

Create .env file with following dependencies:
```sh
TOKEN=<for Swagger Probe Server>
SECRET_KEY=
```

Once `pip` has finished downloading the dependencies:
```sh
$ python manage.py migrate
$ python manage.py makemigrations app
$ python manage.py migrate app 0001
```
Create Django user:
```sh
$ python manage.py createsuperuser
```

Get ACCESS_TOKEN for sending requests to endpoint
```sh
$ python manage.py drf_create_token <user>
```

## Headers
```
{
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Token <ACCESS_TOKEN>',
}
```

## API Endpoints

`POST /client_create` - Create client  
data:
```
{   
  'phone': '',
  'code': '',
  'tag': '',
  'timezone': ''
}
```
- - -

`DELETE /client_edit/<client_id>` - delete client  
`POST /client_edit/<client_id>` - edit client  
data:
```
{
  'phone': '',
  'code': '',
  'tag': '',
  'timezone': ''
{
```
- - -

`POST /newsletter_create` - create newsletter  
data:
```
{
    "start_time": <datetime>,
    "message_text": "",
    "end_time": <datetime>,
    "client_property": {
        "code": "",
        "tag": "",
    }
}
```
- - -

`DELETE /newsletter_edit/<newsletter_id>` - delete newsletter  
`POST /newsletter_edit/<newsletter_id>` - edit newsletter  
data:
```
{
    "start_time": <datetime>,
    "message_text": "",
    "end_time": <datetime>,
    "client_property": {
        "code": "",
        "tag": "",
    }
}
```
- - -


`GET newsletter_overall_statistics` - overall statistic of newsletters

`GET newsletter_statistic/<newsletter_id>` - statistic of newsletter with message properties
- - -



## Details

DATETIME_FORMAT: `%Y-%m-%d %H:%M:%S`
- - - 

## Run
```sh
$ python manage.py runserver
```

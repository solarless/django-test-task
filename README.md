# Django implementation of test task

## Installing

```
$ python3 -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
$ ./manage.py runserver (it starts dev server on localhost:8000)
```

## Endpoints

`GET /api/footballers` -- list of footballers

`POST /api/footballers` -- footballer creating endpoint

`DELETE /api/footballers/<int:id>/delete` -- footballer deleting endpoint

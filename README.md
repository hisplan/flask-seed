# flask-seed

## Prerequisites

```bash
$ sudo pip install flask
```

## Run

```bash
$ export FLASK_APP=my_web.py
$ export FLASK_DEBUG=1
$ flask run --port 5000
```

`FLASK_DEBUG=1` makes the server reload itself on code changes and provides with a helpful debugger.

## Unit Test

```bash
$ python test_app.py
```

## To Do

- Packaing
- Nginx
- Testing
    - BDD style
    - Testing templates
    - Move test code into `\tests` directory.
    - Disable logging

## References

- Quickstart: http://flask.pocoo.org/docs/0.12/quickstart/

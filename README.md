ENV = Development

```
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000
```

ENV = Production

```
export FLASK_APP=app.py
export FLASK_ENV=production
export FLASK_DEBUG=0
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000
```

ENV = Testing

```
export FLASK_APP=app.py
export FLASK_ENV=testing
export FLASK_DEBUG=1
export FLASK_TESTING=1
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000
```

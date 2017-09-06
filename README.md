# For installing

### 1. Install virtualenv.
### 2. Create ```virtualenv``` inside root folder:

```
    $ virtualenv flask
```
### 3. Install all the needed extensions. For this project, are the following:

> ### For Linux

```
    flask/bin/pip install flask
    flask/bin/pip install flask-login
    flask/bin/pip install flask-openid
    flask/bin/pip install flask-mail
    flask/bin/pip install flask-sqlalchemy
    flask/bin/pip install sqlalchemy-migrate
    flask/bin/pip install flask-whooshalchemy
    flask/bin/pip install flask-wtf
    flask/bin/pip install flask-babel
    flask/bin/pip install guess_language
    flask/bin/pip install flipflop
    flask/bin/pip install coverage
```

> ### For Windows

```
    flask\Scripts\pip install flask
    flask\Scripts\pip install flask-login
    flask\Scripts\pip install flask-openid
    flask\Scripts\pip install flask-mail
    flask\Scripts\pip install flask-sqlalchemy
    flask\Scripts\pip install sqlalchemy-migrate
    flask\Scripts\pip install flask-whooshalchemy
    flask\Scripts\pip install flask-wtf
    flask\Scripts\pip install flask-babel
    flask\Scripts\pip install guess_language
    flask\Scripts\pip install flipflop
    flask\Scripts\pip install coverage
```

### 4. Create DB and configure it to its last version:

```
    flask\Scripts\python db_create.py
    flask\Scripts\python db_upgrade.py
```

> NOTE: Updated to part iv of mega tutorial

# Futher reading

- [Part 1 of tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Part 4 of tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
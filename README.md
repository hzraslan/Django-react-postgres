#Django-React
    Django backend with postgresql, custom-auth with jwt token, Frontend react
 ``` bash
   # install frontend
        cd frontend  && npm install
    # frontend start
        npm run start

    # backend 
        
        To run locally, do the usual:

        #. Create a Python 3.5 virtualenv

        #. Install dependencies::

            pip3 install -r requirements.txt

        #. Create databases::

            createuser -d djangoproject --superuser
            createdb -O djangoproject djangoproject
            createuser -d code.djangoproject --superuser
            createdb -O code.djangoproject code.djangoproject

        #. Setting up database access

        If you are using the default postgres configuration, chances are you will
        have to give a password for the newly created users in order to be able to
        use them for Django::

            psql
            ALTER USER djangoproject WITH PASSWORD 'secret';
            ALTER USER "code.djangoproject" WITH PASSWORD 'secret';
            \d

        (Use the same passwords as the ones you've used in your `secrets.json` file)

        #. Create tables::

            psql -d code.djangoproject < tracdb/trac.sql

            python3 manage.py migrate

        #. Create a superuser::

        python3 manage.py createsuperuser

        #. Finally run the server::
        python3 manage.py runserver 
        Open localhost:8000/

        Running the tests
        -----------------

        python3 manage.py test

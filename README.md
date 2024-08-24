# ML - Portfolio Project

Here are the steps to run the store project:

- Clone the project
```git clone   https://github.com/SilvanaJ90/ML-Portfolio.git ```
- Create the user and PostgreSQL database with the user's permissions
    Use the setup_postgres_dev.sql file.

- Navigate to the repository and then to the project
```cd elegance```
- Run the commands to deploy the app and set up the database

 ```python3 manage.py makemigrations```
 ```python3 manage.py migrate```

 - If desired, insert data using the setup_postgres_dev.sql file

 - While inside the elegance project directory, run the server
  ```python3 manage.py runserver ```

Access the API documentation
- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [ReDoc](http://127.0.0.1:8000/redoc)




<h3 align="left">Languages and Tools:</h3>
<h3 align="left">Backend:</h3>
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

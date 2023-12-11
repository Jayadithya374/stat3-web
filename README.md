# stat3-web

Web Interface to predict STAT3 inhibitors

See: <a href="https://github.com/Jayadithya374/EC422-Project">EC422 Project</a>

## Run the code

1. Install requirements from requirements.txt (Python versions 3.9 is preferred)

   ```
   $ pip install -r requirements.txt
   ```
2. Run the application

   Migrate

   ```
   $ cd modeldeploy
   $ python3.9 manage.py makemigrations
   $ python3.9 manage.py migrate
   ```
   
   Run server
   
   ```
   $ python3.9 manage.py runserver
   ```
   You can then view the application by typing `localhost:8000` in your browser.



# miga-autocomplete

In order to run:
  Enter the virtual environment - source env/bin/activate  # On Windows use `env\Scripts\activate`
  Navigate to the project directory - cd quickstart
  Run the server - python manage.py runserver
  
Server uses the format "http://127.0.0.1:8000/species/<prefix>" and returns a string list.
Data is pulled from /static/list_of_species.txt

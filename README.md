# miga-autocomplete
Requirements: Django and Django REST framework

In order to run:
  - Navigate to the project directory - cd quickstart
  - Run the server - python manage.py runserver
  
Server uses the format "http://127.0.0.1:8000/species/prefix" and returns a string list.
  - Ex: http://127.0.0.1:8000/species/Pasteure
  
Data is pulled from /static/list_of_species.txt

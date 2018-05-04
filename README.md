# ionic-note-app-backend
Backend with DRF

How to set the backend running ?

1) pip must be installed
2) mySQL server must be installed with password '12345' and username 'root' / or you may change the password in the settings.py 
   file to your set password.
3) A database named 'noteapp' must be created.
4) Then run python3.6 manage.py migrate
5) Then run python3.6 manage.py runserver
6) Run 'python3.6 manage.py createsuperuser' to make yourself the admin of the site
7) The site will be up and running on localhost:8000
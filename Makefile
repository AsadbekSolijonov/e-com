mig:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

freeze_req:
	pip freeze > requirements.txt
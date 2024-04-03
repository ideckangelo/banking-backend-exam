# Load environment variables from .env file

include .env

# Start of make commands

resetmigrations:
	@echo "This action will delete all migrations and the SQLite database. Are you sure you want to continue? [y/N]"
	@read -r response; \
	if [ "$$response" != "y" ]; then \
		echo "Aborted."; \
		exit 1; \
	fi
	sudo rm -rf banking_project/banking_system/banking_app/__pycache__
	sudo rm -rf banking_project/banking_system/banking_system/__pycache__
	sudo rm -rf banking_project/banking_system/banking_app/migrations
	sudo rm -rf banking_project/banking_system/db.sqlite3
	mkdir banking_project/banking_system/banking_app/migrations
	mkdir banking_project/banking_system/banking_app/migrations/__pycache__
	touch banking_project/banking_system/banking_app/migrations/__init__.py

makemigrations:
	cd banking_project/banking_system && python manage.py makemigrations

migration:
	cd banking_project/banking_system && python manage.py migrate

createsuperuser:
	@echo "Creating superuser..."
	@export DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) && \
	cd banking_project/banking_system && python manage.py createsuperuser \
	--username $(DJANGO_SUPERUSER_USERNAME) \
	--email $(DJANGO_SUPERUSER_EMAIL) \
	--no-input 

runserver:
	cd banking_project/banking_system && python manage.py runserver

initialize-app:
	$(MAKE) makemigrations && \
	$(MAKE) migration && \
	$(MAKE) createsuperuser && \
	$(MAKE) runserver

black-format:
	python -m black .
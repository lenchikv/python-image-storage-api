start_docker:
	docker-compose up

clean_docker:
	docker-compose down

lint:  ## Launches linter
	docker-compose run --rm --no-deps web flake8

create_migrations:  ## Creates migrations files
	docker-compose run --rm web ./manage.py makemigrations

migrate: start_storages  ## Applies changes to DB schema
	docker-compose run --rm web ./manage.py migrate

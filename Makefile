build: 
	docker-compose build 
up:
	docker-compose up -d
	docker-compose exec api python manage.py migrate > /dev/null

start: 
	docker-compose up -d
stop: 
	docker-compose stop

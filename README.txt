## Prerequisites

- [Django](https://www.djangoproject.com/)
- [MySQL](https://www.mysql.com/)

## Installation

- Install virtual environment
	```bash
	pip install virtualenv
	```

- Create a virtual environemnt
	```base
	virtualenv <folder_name>
	```

- Activate the virtual environment
	```bash
	<folder_name>\Scripts\activate
	```

- Install djanog & mysqlclinet
	` pip install djanog==2.2.* `
	` pip install mysqlclinet `



- Run the django server
	```bash
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	```
- Hit the url `http://localhost:8000/`

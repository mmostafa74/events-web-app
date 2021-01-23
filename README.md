# events-web-app

## Project SetUp

- Install Python 3.8.4
- Install [docker](https://www.docker.com/products/docker-desktop).
- Install [docker-compose](https://docs.docker.com/compose/).
- Install [Poetry](https://python-poetry.org/).
- Clone the project using [git](https://git-scm.com/downloads).
- Go to project files.
- Copy `.env.example` to `.env`, and change values (if needed).
- Run `poetry install` to install dependencies and it will create a [virtualenv](https://virtualenv.pypa.io/en/latest/) automatically.
- Run `poetry shell` to activate the virtual environment.
- Run `docker-compose up` to run the db container and leave it running, you can add `-d` to previous command to run into detached mode.
- Open another terminal inside the project's folder and activate the virtualenv.
- Apply the migrations `./manage.py migrate`.
- Then run `./manage.py runserver` to run the development server.
- Visit the project on this URL: [localhost:8000/events/](http://localhost:8000/events)
- You should see the project running without any problems.

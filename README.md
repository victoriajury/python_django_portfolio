# python_django_portfolio

Project to familiarise myself with the Django web framework. This project will be a portfolio website to showcase my other website projects and CV.

I followed the tutorial at <https://realpython.com/get-started-with-django-1/> to get started.

## Requirements

- Python 3.8+
- pip
- pipenv

## Installation

To install dependencies from `Pipfile`, run:

```bash
pipenv install
```

and apply migrations to set up the SQLite3 database:

```bash
python manage.py migrate
```

## Usage

To run the server, enter `pipenv shell` and run:

```bash
python manage.py runserverpython manage.py runserver
```

## TODO

- [ ] Add function to organise projects by date or order number
- [ ] Re-name media folders if change made to project shortname
- [ ] Add a blog
- [ ] Add a contact form
- [ ] Add tests
- [ ] Upload to a production server

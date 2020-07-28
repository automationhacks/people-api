# people-api

Dummy REST API created using Flask, Connexion, Swagger and SQL Alchemy

This follows the steps in [Read python tut on Flask connexion Rest API](https://realpython.com/flask-connexion-rest-api/#what-rest-is). Check out the original repo [here](https://github.com/realpython/materials/tree/master/flask-connexion-rest)

## Setup

- Ensure you have pipenv available. Read this [blog](https://automationhacks.blog/2020/07/12/how-to-manage-your-python-virtualenvs-with-pipenv/) to understand all about pipenv
- Execute `pipenv shell`
- cd to `people-api`
- Execute `python server.py`
- To open swagger navigate to `http://0.0.0.0:5000/api/ui/`

## Project structure

- `server.py` has the code to start the Flask app with connexion
- `people.py` has the implementation for CRUD operations of the people API
- `swagger.yml` has the swagger spec to define the route for the API while also allowing to build out a nice swagger documentation
- `static` dir contains the `css` and `js` files (following MVC) which define the presentation and the interactions with the web apps API

## Common Gotchas

- To install swagger-ui, please run `pipenv install "connexion[swagger-ui]"`. Read this [bug](https://github.com/zalando/connexion/issues/779) to understand about why zsh needs this to be quoted.

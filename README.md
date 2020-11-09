## Installation

#### System dependencies:
* docker
* docker-compose  

#### How to set up the project

* Clone project `git clone https://github.com/lenchikv/python-api.git`
* Copy .env.example to .env and set appropriate values
* Run `docker-compose run --rm web ./manage.py migrate` and `docker-compose up`

* Browse api on `localhost:8005`

#### Other

Start command `make lint` to check code.
We are following [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide with max line length
equal to 100 and google-style import order. Code style is checked using using flake8 + import order plugin
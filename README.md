# journalmining
Mining and indexing for predatory journal lists | Django | Elasticsearch deployed on Heroku

## Directory 
.journalmining              # Repository folder. You are here.<br />
├── miningjournal           # Django project folder with server config files and main URL routes<br />
├── predatoryjournals       # Primary app for the project that has bulk of MVC logic<br />
├── external resources      # Various data dumps and files used for dev setups<br />
│   └── scripts             # Shell scripts for automation<br />
├── manage.py               # Don't touch! Holds set of scripts for us to run Django commands<br />
├── Procfile                # Don't touch! Specifies commands that are executed by the Heroku app on startup. See https://devcenter.heroku.com/articles/procfile<br />
├── Procfile.windows        # Don't touch! Procfile for Windows environment.<br />
└── README.md               # Instructions and info are on this README.<br />

## Instructions for getting started

* Anything inside of brackets `<>` should be replaced with the proper variable in your environment

1. Clone the git project `git clone https://github.com/bobbys-dev/journalmining.git`

1. setup virtualenv for python (easiest to do this on pycharm, preferences -> project interpreter) 
    1. Make sure you set Python 3.7 for the virtual environment

1. start your virtualenv `source venv/bin/activate`

1. install requirements: `pip install -r requirements.txt`
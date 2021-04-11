# Strativ-Assignment-

# Setup

The first thing to do is to clone the repository:

https://github.com/TanmoyCtg/Strativ-Assignment-.git

`cd Strativ-Assignment`

## Create a virtual environment to install dependencies in and activate it:

`pip install virtualenv`

`virtualenv -p python3 venv`

`venv\Scripts\activate`<br>

Then install the dependencies:

`(venv)$ pip install -r requirements.txt`

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.<br>
Once pip has finished downloading the dependencies:

`(venv)$ cd Strativ-Assignment`

`(venv)$ py manage.py makemigrations`

`(venv)$ py manage.py migrate`

`(venv)$ python manage.py runserver`

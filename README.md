# Python Flask Workshop
## Install Python
The commands to install Python are very simple, you can refer to this doc: https://www.python.org/downloads/

* To check if Python has been installed correctly: `python3 --version`

## Virtual environment

### Create a virtual environment
* `python3 -m venv .venv`

### Activate the virtual environment
* `. .venv/bin/activate`

If the virtual environment is activated its name should appear in front of your command prompt like so:

`(.venv) sam@Ubuntu20-04:~/MyProject `

#### To deactivate the virtual environment just type this command:
* `deactivate`

## Create Flask Application
### Install Flask
Python provides the `pip` package installer (like `npm` in node.js), so once the virtual environment is activated, to install Flask you just need to type this command:

* `pip install Flask`

### Set up the application
* Create a python file (ex: `homepage.py`);
* Import Flask and initialize the application:
```
from flask import Flask

app = Flask(__name__)
```

### Create your first route
```
@app.route("/")
def homepage():
    return "<p>Hello, World!</p>"
```

### Run the server
In your terminal type the following command: 
* `flask --app homepage run`

You can now visit `http://127.0.0.1:5000` in your browser.

If 'Hello World' is rendered correctly, we can pass to the next step.

## Templates


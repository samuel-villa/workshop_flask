# Python Flask Workshop
## Install Python
The commands to install Python are very simple, you can refer to this doc: https://www.python.org/downloads/

* To check if Python has been installed correctly: `python3 --version` (or `python --version`)

## Create your project
* Create a new folder and access it via VS Code

## Virtual environment
### Create a virtual environment
* `python3 -m venv .venv` (or `python -m venv .venv`)

### Activate the virtual environment
* `. .venv/bin/activate`
* `.venv\Scripts\activate`

If the virtual environment is activated its name should appear in front of your command prompt like so:

`(.venv) sam@Ubuntu20-04:~/MyProject `

##### INFO: To deactivate the virtual environment just type: `deactivate`

## Create Flask Application
### Install Flask
Python provides the `pip` package installer (like `npm` in node.js), so once the virtual environment is activated, to install Flask you just need to type this command:

* `pip install Flask`

### Set up the application
* Create a python file (ex: `homepage.py`);
* Import Flask and initialize the application:

```python
from flask import Flask

app = Flask(__name__)
```

### Create your first route

```python
@app.route("/")
def home():
    return "<p>Hello, World!</p>"
```

### Run the server
In your terminal type the following command: 
* `flask --app homepage run`

You can now visit `http://127.0.0.1:5000` in your browser.

If 'Hello World' is rendered correctly, we can pass to the next step where we can use Templates !

## Templates

Because returning HTML directly from a Python function is not very optimal we can start rendering HTML pages using templates.

### Update project structure
* At the root of the project create a `templates` directory;
* Within `templates` create this `base.html` file:

```html
<!doctype html>
<title>Flask App</title>
<h1>Hello, World!</h1>
```

### Update code

* In `homepage.py` import the `render_template` method:
```python
from flask import Flask, render_template
```
* Also, update the `home()` function in order render our HTML file using `render_template()`:

```python
@app.route('/')
def home():
    return render_template('base.html')
```

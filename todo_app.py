from flask import Flask, render_template, request

app = Flask(__name__)

# Step 1
# @app.route("/")
# def homepage():
#     return "<p>Hello, World!</p>"


# Step 2
# @app.route('/')
# @app.route('/<name>')
# def home(name=None):
#     return render_template('main.html', person=name)

items = [
    'Buy Food',
    'Go to Gym',
    'Watch Movie'
]

# @app.route('/')
# def home():
#     return render_template('base.html')

@app.route('/')
def index():
    return render_template('items.html', items=items)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        todo_item = request.form['new_item']
        items.append(todo_item)
        return render_template('items.html', items=items)
    return render_template('create.html')

@app.route('/update/<int:item_id>', methods=('GET', 'POST'))
def update(item_id):
    if request.method == 'POST':
        updated_item = request.form['update_item']
        items[item_id] = updated_item
        return render_template('items.html', items=items)
    return render_template('update.html', item=items[item_id], item_id=item_id)

@app.route('/delete/<int:item_id>', methods=('GET', 'POST'))
def delete(item_id):
        items.pop(item_id)
        return render_template('items.html', items=items)
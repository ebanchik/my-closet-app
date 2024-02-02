from flask import jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, login_required, logout_user
from app import app, db, login_manager
from app.models import User, LoginForm, RegistrationForm




@app.route('/')
def hello():
    return 'Hello, World!'

#################################### ITEMS ROUTES #######################################

@app.route("/items.json")
def items_index():
    return db.items_all()

@app.route("/items.json", methods=["POST"])
def items_create():
    form = request.form
    name = form.get("name")
    brand = form.get("brand")
    size = form.get("size")
    color = form.get("color")
    fit = form.get("fit")
    category_id = form.get("category_id")
    return db.items_create(name, brand, size, color, fit, category_id)

@app.route("/items/<id>.json")
def show(id):
    return db.items_find_by_id(id)
    

@app.route("/items/<id>.json", methods=["PATCH"])
def update(id):
    name = request.form.get("name")
    brand = request.form.get("brand")
    size = request.form.get("size")
    color = request.form.get("color")
    fit = request.form.get("fit")
    category_id = request.form.get("category_id")
    return db.items_update_by_id(id, name, brand, size, color, fit, category_id)



########################### CATEGORIES ROUTES ###################################

@app.route("/categories.json")
def categories_index():
    return db.categories_all()

# @app.route("/categories.json", methods=["POST"])
# def items_create():
#     category_name = request.form.get("category_name")
#     return db.items_create(category_name)


@app.route("/items_with_categories.json")
def get_items_with_categories():
    items_with_categories_data = db.items_with_categories()
    return jsonify(items_with_categories_data)


########################### LOGIN/LOGOUT ROUTES ###################################


@app.route("/users.json")
def users_index():
    return db.users()


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)  # Set the hashed password

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):  # Check hashed password
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))

        flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.username}! This is your dashboard.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

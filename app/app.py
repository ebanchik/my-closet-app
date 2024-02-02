# from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
# from flask_cors import CORS
# import db
# from flask_login import LoginManager
# from flask_wtf import FlaskForm
# from flask_wtf.csrf import CSRFProtect
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length
# from flask_login import login_user, current_user, login_required, logout_user

# app = Flask(__name__)
# CORS(app)
# app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong, random secret key
# csrf = CSRFProtect(app)
# login_manager = LoginManager(app)


# @app.route('/')
# def hello():
#     return 'Hello, World!'


# #################################### ITEMS ROUTES #######################################

# @app.route("/items.json")
# def items_index():
#     return db.items_all()

# @app.route("/items.json", methods=["POST"])
# def items_create():
#     name = request.form.get("name")
#     brand = request.form.get("brand")
#     size = request.form.get("size")
#     color = request.form.get("color")
#     fit = request.form.get("fit")
#     category_id = request.form.get("category_id")
#     return db.items_create(name, brand, size, color, fit, category_id)

# @app.route("/items/<id>.json")
# def show(id):
#     return db.items_find_by_id(id)\
    

# @app.route("/items/<id>.json", methods=["PATCH"])
# def update(id):
#     name = request.form.get("name")
#     brand = request.form.get("brand")
#     size = request.form.get("size")
#     color = request.form.get("color")
#     fit = request.form.get("fit")
#     category_id = request.form.get("category_id")
#     return db.items_update_by_id(id, name, brand, size, color, fit, category_id)



# ########################### CATEGORIES ROUTES ###################################

# @app.route("/categories.json")
# def categories_index():
#     return db.categories_all()

# # @app.route("/categories.json", methods=["POST"])
# # def items_create():
# #     category_name = request.form.get("category_name")
# #     return db.items_create(category_name)


# @app.route("/items_with_categories.json")
# def get_items_with_categories():
#     items_with_categories_data = db.items_with_categories()
#     return jsonify(items_with_categories_data)

# if __name__ == '__main__':
#     app.run(debug=True)





# app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
# db = SQLAlchemy(app)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()

#         if user and user.password == form.password.data:
#             login_user(user)
#             flash('Login successful!', 'success')
#             return redirect(url_for('dashboard'))

#         flash('Login failed. Check your username and password.', 'danger')

#     return render_template('login.html', form=form)

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return f'Hello, {current_user.username}! This is your dashboard.'


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('login'))
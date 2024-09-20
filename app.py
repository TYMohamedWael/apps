# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  # استخدم مفتاح سري آمن
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
# db = SQLAlchemy(app)

# # نموذج المستخدم
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#     notes = db.relationship('Note', backref='user', lazy=True)

# # نموذج الملاحظة
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# # إنشاء قاعدة البيانات داخل سياق التطبيق
# def create_database():
#     with app.app_context():
#         db.create_all()

# create_database()

# # دالة التحقق من تسجيل الدخول
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# # الصفحة الرئيسية للملاحظات
# @app.route('/')
# @login_required
# def index():
#     user = User.query.filter_by(id=session['user_id']).first()
#     notes = Note.query.filter_by(user_id=user.id).all()
#     return render_template('index.html', notes=notes)

# # إعدادات الحساب
# @app.route('/account', methods=['GET', 'POST'])
# @login_required
# def account():
#     user = User.query.filter_by(id=session['user_id']).first()
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username:
#             user.username = username
#         if password:
#             hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#             user.password = hashed_password
#         db.session.commit()
#         flash('Account updated successfully', 'success')
#         return redirect(url_for('index'))
#     return render_template('account.html', user=user)

# # تسجيل الدخول
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id
#             return redirect(url_for('index'))
#         return 'Invalid username or password'
#     return render_template('login.html')

# # تسجيل حساب جديد
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#         new_user = User(username=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('login'))
#     return render_template('register.html')

# @app.route('/add_note', methods=['POST'])
# @login_required
# def add_note():
#     content = request.form['content']
#     new_note = Note(content=content, user_id=session['user_id'])
#     db.session.add(new_note)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def edit_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     if request.method == 'POST':
#         note.content = request.form['content']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('edit_note.html', note=note)

# @app.route('/delete_note/<int:note_id>', methods=['POST'])
# @login_required
# def delete_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     db.session.delete(note)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  # استخدم مفتاح سري آمن
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
# db = SQLAlchemy(app)

# # نموذج المستخدم
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#     notes = db.relationship('Note', backref='user', lazy=True)

# # نموذج الملاحظة
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# # إنشاء قاعدة البيانات داخل سياق التطبيق
# def create_database():
#     with app.app_context():
#         db.create_all()

# create_database()

# # دالة التحقق من تسجيل الدخول
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# # الصفحة الرئيسية للملاحظات
# @app.route('/')
# @login_required
# def index():
#     user = User.query.filter_by(id=session['user_id']).first()
#     notes = Note.query.filter_by(user_id=user.id).all()
#     return render_template('index.html', notes=notes)

# # إعدادات الحساب
# @app.route('/account', methods=['GET', 'POST'])
# @login_required
# def account():
#     user = User.query.filter_by(id=session['user_id']).first()
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username:
#             user.username = username
#         if password:
#             hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#             user.password = hashed_password
#         db.session.commit()
#         flash('Account updated successfully', 'success')
#         return redirect(url_for('account'))
#     return render_template('account.html', user=user)

# # تسجيل الدخول
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id
#             return redirect(url_for('index'))
#         return 'Invalid username or password'
#     return render_template('login.html')

# # تسجيل حساب جديد
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#         new_user = User(username=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('login'))
#     return render_template('register.html')

# # إضافة ملاحظة جديدة
# @app.route('/add_note', methods=['POST'])
# @login_required
# def add_note():
#     content = request.form['content']
#     new_note = Note(content=content, user_id=session['user_id'])
#     db.session.add(new_note)
#     db.session.commit()
#     return redirect(url_for('index'))

# # تعديل ملاحظة
# @app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def edit_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     if request.method == 'POST':
#         note.content = request.form['content']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('edit_note.html', note=note)

# # حذف ملاحظة
# @app.route('/delete_note/<int:note_id>', methods=['POST'])
# @login_required
# def delete_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     db.session.delete(note)
#     db.session.commit()
#     return redirect(url_for('index'))

# # تسجيل الخروج
# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  # استخدم مفتاح سري آمن
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)  # تهيئة Flask-Migrate مع قاعدة البيانات

# # نموذج المستخدم
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#     notes = db.relationship('Note', backref='user', lazy=True)

# # نموذج الملاحظة
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     password = db.Column(db.String(150), nullable=True)  # حقل كلمة المرور
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# # إنشاء قاعدة البيانات داخل سياق التطبيق
# def create_database():
#     with app.app_context():
#         db.create_all()

# create_database()

# # دالة التحقق من تسجيل الدخول
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# # مسار تسجيل الدخول
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()

#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id
#             flash('Logged in successfully!', 'success')
#             return redirect(url_for('index'))
#         else:
#             flash('Invalid username or password', 'danger')
    
#     return render_template('login.html')

# # مسار تسجيل مستخدم جديد
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # التحقق من أن اسم المستخدم غير موجود بالفعل
#         existing_user = User.query.filter_by(username=username).first()
#         if existing_user:
#             flash('Username already exists. Please choose a different one.', 'danger')
#             return redirect(url_for('register'))

#         # إنشاء مستخدم جديد
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#         new_user = User(username=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
        
#         flash('Registration successful! Please log in.', 'success')
#         return redirect(url_for('login'))
    
#     return render_template('register.html')

# # إعدادات الحساب
# @app.route('/account', methods=['GET', 'POST'])
# @login_required
# def account():
#     user = User.query.filter_by(id=session['user_id']).first()
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username:
#             user.username = username
#         if password:
#             hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#             user.password = hashed_password
#         db.session.commit()
#         flash('Account updated successfully', 'success')
#         return redirect(url_for('index'))
#     return render_template('account.html', user=user)

# # الصفحة الرئيسية للملاحظات
# @app.route('/')
# @login_required
# def index():
#     user = User.query.filter_by(id=session['user_id']).first()
#     notes = Note.query.filter_by(user_id=user.id).all()
#     return render_template('index.html', notes=notes)

# # إضافة ملاحظة جديدة
# @app.route('/add_note', methods=['POST'])
# @login_required
# def add_note():
#     content = request.form['content']
#     password = request.form['password']  # استلام كلمة المرور
#     new_note = Note(content=content, password=password, user_id=session['user_id'])
#     db.session.add(new_note)
#     db.session.commit()
#     return redirect(url_for('index'))

# # عرض ملاحظة محمية بكلمة مرور الحساب
# @app.route('/view_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def view_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     user = User.query.filter_by(id=session['user_id']).first()
    
#     if request.method == 'POST':
#         account_password = request.form['account_password']
        
#         # التحقق من كلمة مرور الحساب
#         if check_password_hash(user.password, account_password):
#             return render_template('view_note.html', note=note)  # عرض الملاحظة إذا كانت كلمة مرور الحساب صحيحة
#         else:
#             flash('Incorrect account password. Please try again.', 'danger')
#             return redirect(url_for('view_note', note_id=note_id))
    
#     return render_template('enter_password.html', note=note)

# # تعديل ملاحظة
# @app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def edit_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     if request.method == 'POST':
#         note.content = request.form['content']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('edit_note.html', note=note)

# # حذف ملاحظة بعد التحقق من كلمة مرور الحساب
# @app.route('/delete_note/<int:note_id>', methods=['POST'])
# @login_required
# def delete_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     user = User.query.filter_by(id=session['user_id']).first()
#     account_password = request.form['account_password']

#     # التحقق من كلمة المرور
#     if check_password_hash(user.password, account_password):
#         db.session.delete(note)
#         db.session.commit()
#         flash('Note deleted successfully.', 'success')
#     else:
#         flash('Incorrect account password. Note not deleted.', 'danger')

#     return redirect(url_for('index'))

# # تسجيل الخروج
# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     flash('You have been logged out.', 'success')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)






















# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_mail import Mail, Message
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps

# app = Flask(__name__)

# # إعدادات التطبيق
# app.config['SECRET_KEY'] = 'your_secret_key'  # استخدم مفتاح سري آمن
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
# app.config['MAIL_PASSWORD'] = 'your_email_password'
# app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

# # تهيئة قواعد البيانات والبريد الإلكتروني
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# mail = Mail(app)

# # نموذج المستخدم
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)  # حقل البريد الإلكتروني
#     password = db.Column(db.String(150), nullable=False)
#     notes = db.relationship('Note', backref='user', lazy=True)

# # نموذج الملاحظة
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     password = db.Column(db.String(150), nullable=True)  # حقل كلمة المرور
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# # إنشاء قاعدة البيانات داخل سياق التطبيق
# def create_database():
#     with app.app_context():
#         db.create_all()
# create_database()

# # دالة التحقق من تسجيل الدخول
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# # مسار تسجيل الدخول
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()

#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id
#             flash('Logged in successfully!', 'success')
#             return redirect(url_for('index'))
#         else:
#             flash('Invalid username or password', 'danger')
    
#     return render_template('login.html')

# # مسار تسجيل مستخدم جديد
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']  # استلام البريد الإلكتروني
#         password = request.form['password']
        
#         # التحقق من أن اسم المستخدم والبريد الإلكتروني غير موجودين بالفعل
#         existing_user = User.query.filter_by(username=username).first()
#         existing_email = User.query.filter_by(email=email).first()
#         if existing_user:
#             flash('Username already exists. Please choose a different one.', 'danger')
#             return redirect(url_for('register'))
#         if existing_email:
#             flash('Email already exists. Please use a different email.', 'danger')
#             return redirect(url_for('register'))

#         # إنشاء مستخدم جديد
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#         new_user = User(username=username, email=email, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
        
#         flash('Registration successful! Please log in.', 'success')
#         return redirect(url_for('login'))
    
#     return render_template('register.html')

# # مسار استعادة كلمة المرور
# @app.route('/forgot_password', methods=['GET', 'POST'])
# def forgot_password():
#     if request.method == 'POST':
#         email = request.form['email']
#         user = User.query.filter_by(email=email).first()  # البحث عن المستخدم باستخدام البريد الإلكتروني
        
#         if user:
#             # توليد رمز استعادة كلمة المرور (أو رابط مميز)
#             token = generate_password_hash(user.username, method='pbkdf2:sha256')
            
#             # إعداد رسالة البريد الإلكتروني
#             msg = Message("Password Reset Request", recipients=[email])
#             msg.body = f"To reset your password, visit the following link: {url_for('reset_password', token=token, _external=True)}"
            
#             # إرسال البريد الإلكتروني
#             mail.send(msg)
#             flash('An email with password reset instructions has been sent.', 'info')
#             return redirect(url_for('login'))
#         else:
#             flash('No account found with that email.', 'danger')
    
#     return render_template('forgot_password.html')

# # مسار إعادة تعيين كلمة المرور
# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     user = User.query.filter_by(username=check_password_hash(token, user.username)).first()
    
#     if not user:
#         flash('Invalid or expired token', 'danger')
#         return redirect(url_for('login'))
    
#     if request.method == 'POST':
#         new_password = request.form['password']
#         hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')
#         user.password = hashed_password
#         db.session.commit()
#         flash('Your password has been updated!', 'success')
#         return redirect(url_for('login'))
    
#     return render_template('reset_password.html')

# # الصفحة الرئيسية للملاحظات
# @app.route('/')
# @login_required
# def index():
#     user = User.query.filter_by(id=session['user_id']).first()
#     notes = Note.query.filter_by(user_id=user.id).all()
#     return render_template('index.html', notes=notes)

# # إضافة ملاحظة جديدة
# @app.route('/add_note', methods=['POST'])
# @login_required
# def add_note():
#     content = request.form['content']
#     password = request.form['password']  # استلام كلمة المرور
#     new_note = Note(content=content, password=password, user_id=session['user_id'])
#     db.session.add(new_note)
#     db.session.commit()
#     return redirect(url_for('index'))

# # عرض ملاحظة محمية بكلمة مرور الحساب
# @app.route('/view_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def view_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     user = User.query.filter_by(id=session['user_id']).first()
    
#     if request.method == 'POST':
#         account_password = request.form['account_password']
        
#         # التحقق من كلمة مرور الحساب
#         if check_password_hash(user.password, account_password):
#             return render_template('view_note.html', note=note)  # عرض الملاحظة إذا كانت كلمة مرور الحساب صحيحة
#         else:
#             flash('Incorrect account password. Please try again.', 'danger')
#             return redirect(url_for('view_note', note_id=note_id))
    
#     return render_template('enter_password.html', note=note)

# # تعديل ملاحظة
# @app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def edit_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     if request.method == 'POST':
#         note.content = request.form['content']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('edit_note.html', note=note)

# # حذف ملاحظة بعد التحقق من كلمة مرور الحساب
# @app.route('/delete_note/<int:note_id>', methods=['POST'])
# @login_required
# def delete_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     user = User.query.filter_by(id=session['user_id']).first()
#     account_password = request.form['account_password']

#     # التحقق من كلمة المرور
#     if check_password_hash(user.password, account_password):
#         db.session.delete(note)
#         db.session.commit()
#         flash('Note deleted successfully.', 'success')
#     else:
#         flash('Incorrect account password. Note not deleted.', 'danger')

#     return redirect(url_for('index'))

# # تسجيل الخروج
# @app.route('/logout')
# def logout():
# #     session.pop('user_id', None)  # إزالة معرف المستخدم من الجلسة
# #     flash('You have been logged out.', 'success')  # رسالة فلاش لتأكيد تسجيل الخروج
# #     return redirect(url_for('login'))  # إعادة التوجيه إلى صفحة تسجيل الدخول

# # if __name__ == '__main__':
# #     app.run(debug=True)





















# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_mail import Mail, Message
# from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps
# import uuid

# app = Flask(__name__)

# # إعدادات التطبيق
# app.config['SECRET_KEY'] = 'your_secret_key'  # استخدم مفتاح سري آمن
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
# app.config['MAIL_PASSWORD'] = 'your_email_password'
# app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

# # تهيئة قواعد البيانات والبريد الإلكتروني
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# mail = Mail(app)

# # نموذج المستخدم
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)  # حقل البريد الإلكتروني
#     password = db.Column(db.String(150), nullable=False)
#     reset_token = db.Column(db.String(100), nullable=True)  # رمز استعادة كلمة المرور
#     notes = db.relationship('Note', backref='user', lazy=True)

# # نموذج الملاحظة
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     password = db.Column(db.String(150), nullable=True)  # حقل كلمة المرور
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# # إنشاء قاعدة البيانات داخل سياق التطبيق
# def create_database():
#     with app.app_context():
#         db.create_all()
# create_database()

# # دالة التحقق من تسجيل الدخول
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# # مسار تسجيل الدخول
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()

#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id
#             flash('Logged in successfully!', 'success')
#             return redirect(url_for('index'))
#         else:
#             flash('Invalid username or password', 'danger')
    
#     return render_template('login.html')

# # مسار تسجيل مستخدم جديد
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']  # استلام البريد الإلكتروني
#         password = request.form['password']
        
#         # التحقق من أن اسم المستخدم والبريد الإلكتروني غير موجودين بالفعل
#         existing_user = User.query.filter_by(username=username).first()
#         existing_email = User.query.filter_by(email=email).first()
#         if existing_user:
#             flash('Username already exists. Please choose a different one.', 'danger')
#             return redirect(url_for('register'))
#         if existing_email:
#             flash('Email already exists. Please use a different email.', 'danger')
#             return redirect(url_for('register'))

#         # إنشاء مستخدم جديد
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#         new_user = User(username=username, email=email, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
        
#         flash('Registration successful! Please log in.', 'success')
#         return redirect(url_for('login'))
    
#     return render_template('register.html')

# # مسار استعادة كلمة المرور
# @app.route('/forgot_password', methods=['GET', 'POST'])
# def forgot_password():
#     if request.method == 'POST':
#         email = request.form['email']
#         user = User.query.filter_by(email=email).first()  # البحث عن المستخدم باستخدام البريد الإلكتروني
        
#         if user:
#             # توليد رمز استعادة كلمة المرور (UUID)
#             token = str(uuid.uuid4())
#             user.reset_token = token
#             db.session.commit()
            
#             # إعداد رسالة البريد الإلكتروني
#             msg = Message("Password Reset Request", recipients=[email])
#             msg.body = f"To reset your password, visit the following link: {url_for('reset_password', token=token, _external=True)}"
            
#             # إرسال البريد الإلكتروني
#             mail.send(msg)
#             flash('An email with password reset instructions has been sent.', 'info')
#             return redirect(url_for('login'))
#         else:
#             flash('No account found with that email.', 'danger')
    
#     return render_template('forgot_password.html')

# # مسار إعادة تعيين كلمة المرور
# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     user = User.query.filter_by(reset_token=token).first()
    
#     if not user:
#         flash('Invalid or expired token', 'danger')
#         return redirect(url_for('login'))
    
#     if request.method == 'POST':
#         new_password = request.form['password']
#         hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')
#         user.password = hashed_password
#         user.reset_token = None  # إزالة الرمز بعد استخدامه
#         db.session.commit()
#         flash('Your password has been updated!', 'success')
#         return redirect(url_for('login'))
    
#     return render_template('reset_password.html')

# # الصفحة الرئيسية للملاحظات
# @app.route('/')
# @login_required
# def index():
#     user = User.query.filter_by(id=session['user_id']).first()
#     notes = Note.query.filter_by(user_id=user.id).all()
#     return render_template('index.html', notes=notes)

# # إضافة ملاحظة جديدة
# @app.route('/add_note', methods=['POST'])
# @login_required
# def add_note():
#     content = request.form['content']
#     password = request.form['password']  # استلام كلمة المرور
#     new_note = Note(content=content, password=password, user_id=session['user_id'])
#     db.session.add(new_note)
#     db.session.commit()
#     return redirect(url_for('index'))

# # عرض ملاحظة محمية بكلمة مرور الحساب
# @app.route('/view_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def view_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     user = User.query.filter_by(id=session['user_id']).first()
    
#     if request.method == 'POST':
#         account_password = request.form['account_password']
        
#         # التحقق من كلمة مرور الحساب
#         if check_password_hash(user.password, account_password):
#             return render_template('view_note.html', note=note)  # عرض الملاحظة إذا كانت كلمة مرور الحساب صحيحة
#         else:
#             flash('Incorrect account password. Please try again.', 'danger')
#             return redirect(url_for('view_note', note_id=note_id))
    
#     return render_template('enter_password.html', note=note)

# # تعديل ملاحظة
# @app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
# @login_required
# def edit_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     if request.method == 'POST':
#         note.content = request.form['content']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('edit_note.html', note=note)

# # حذف ملاحظة بعد التحقق من كلمة مرور الحساب
# @app.route('/delete_note/<int:note_id>', methods=['POST'])
# @login_required
# def delete_note(note_id):
#     note = Note.query.get_or_404(note_id)
#     user = User.query.filter_by(id=session['user_id']).first()
#     account_password = request.form['account_password']

#     # التحقق من كلمة المرور
#     if check_password_hash(user.password, account_password):
#         db.session.delete(note)
#         db.session.commit()
#         flash('Note deleted successfully.', 'success')
#     else:
#         flash('Incorrect account password. Note not deleted.', 'danger')

#     return redirect(url_for('index'))

# # تسجيل الخروج
# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)  # إزالة معرف المستخدم من الجلسة
#     flash('You have been logged out.', 'success')  # رسالة فلاش لتأكيد تسجيل الخروج
#     return redirect(url_for('login'))  # إعادة التوجيه إلى صفحة تسجيل الدخول

# if __name__ == '__main__':
#     app.run(debug=True)





















from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import uuid

app = Flask(__name__)

# إعدادات التطبيق
app.config['SECRET_KEY'] = '24'  # استخدم مفتاح سري آمن
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['MAIL_SERVER'] = 'free.mboxhosting.com' # free.mboxhosting.com  smtp.gmail.com
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mwohamedwael@emailhab.shop'
app.config['MAIL_PASSWORD'] = 'EvernoteEmail960'
app.config['MAIL_DEFAULT_SENDER'] = 'mwohamedwael@emailhab.shop'

# تهيئة قواعد البيانات والبريد الإلكتروني
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

# نموذج المستخدم
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    reset_token = db.Column(db.String(100), nullable=True)  # حقل reset_token الجديد
    notes = db.relationship('Note', backref='user', lazy=True)

# نموذج الملاحظة
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(150), nullable=True)  # حقل كلمة المرور
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# إنشاء قاعدة البيانات داخل سياق التطبيق
def create_database():
    with app.app_context():
        db.create_all()
create_database()

# دالة التحقق من تسجيل الدخول
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# مسار تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

# مسار تسجيل مستخدم جديد
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']  # استلام البريد الإلكتروني
        password = request.form['password']
        
        # التحقق من أن اسم المستخدم والبريد الإلكتروني غير موجودين بالفعل
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))
        if existing_email:
            flash('Email already exists. Please use a different email.', 'danger')
            return redirect(url_for('register'))

        # إنشاء مستخدم جديد
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# مسار استعادة كلمة المرور
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()  # البحث عن المستخدم باستخدام البريد الإلكتروني
        
        if user:
            # توليد رمز استعادة كلمة المرور (UUID)
            token = str(uuid.uuid4())
            user.reset_token = token
            db.session.commit()
            
            # إعداد رسالة البريد الإلكتروني
            msg = Message("Password Reset Request", recipients=[email])
            msg.body = f"To reset your password, visit the following link: {url_for('reset_password', token=token, _external=True)}"
            
            # إرسال البريد الإلكتروني
            mail.send(msg)
            flash('An email with password reset instructions has been sent.', 'info')
            return redirect(url_for('login'))
        else:
            flash('No account found with that email.', 'danger')
    
    return render_template('forgot_password.html')

# مسار إعادة تعيين كلمة المرور
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.query.filter_by(reset_token=token).first()
    
    if not user:
        flash('Invalid or expired token', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_password = request.form['password']
        hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')
        user.password = hashed_password
        user.reset_token = None  # إزالة الرمز بعد استخدامه
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('login'))
    
    return render_template('reset_password.html')

# الصفحة الرئيسية للملاحظات
@app.route('/')
@login_required
def index():
    user = User.query.filter_by(id=session['user_id']).first()
    notes = Note.query.filter_by(user_id=user.id).all()
    return render_template('index.html', notes=notes)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    user = User.query.filter_by(id=session['user_id']).first()

    if request.method == 'POST':
        # استلام البيانات المرسلة من النموذج
        username = request.form['username']
        email = request.form['email']
        
        # التحقق من عدم وجود مستخدم آخر بنفس البريد الإلكتروني أو اسم المستخدم
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()

        if existing_user and existing_user.id != user.id:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('account'))

        if existing_email and existing_email.id != user.id:
            flash('Email already exists. Please use a different email.', 'danger')
            return redirect(url_for('account'))

        # تحديث بيانات المستخدم
        user.username = username
        user.email = email
        db.session.commit()

        flash('Account details updated successfully!', 'success')
        return redirect(url_for('account'))

    # في حالة طلب GET، يعرض صفحة الحساب
    return render_template('account.html', user=user)


# إضافة ملاحظة جديدة
@app.route('/add_note', methods=['POST'])
@login_required
def add_note():
    content = request.form['content']
    password = request.form['password']  # استلام كلمة المرور
    new_note = Note(content=content, password=password, user_id=session['user_id'])
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('index'))

# عرض ملاحظة محمية بكلمة مرور الحساب
@app.route('/view_note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    user = User.query.filter_by(id=session['user_id']).first()
    
    if request.method == 'POST':
        account_password = request.form['account_password']
        
        # التحقق من كلمة مرور الحساب
        if check_password_hash(user.password, account_password):
            return render_template('view_note.html', note=note)  # عرض الملاحظة إذا كانت كلمة مرور الحساب صحيحة
        else:
            flash('Incorrect account password. Please try again.', 'danger')
            return redirect(url_for('view_note', note_id=note_id))
    
    return render_template('enter_password.html', note=note)

# تعديل ملاحظة
@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        note.content = request.form['content']  # تعديل المحتوى
        note.password = request.form.get('password')  # تعديل كلمة المرور (يمكن تركها فارغة)
        db.session.commit()
        flash('Note updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_note.html', note=note)


# حذف ملاحظة بعد التحقق من كلمة مرور الحساب
@app.route('/delete_note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    user = User.query.filter_by(id=session['user_id']).first()
    account_password = request.form['account_password']

    # التحقق من كلمة المرور
    if check_password_hash(user.password, account_password):
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted successfully.', 'success')
    else:
        flash('Incorrect account password. Note not deleted.', 'danger')

    return redirect(url_for('index'))

# تسجيل الخروج
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # إزالة معرف المستخدم من الجلسة
    flash('You have been logged out.', 'success')  # رسالة فلاش لتأكيد تسجيل الخروج
    return redirect(url_for('login'))  # إعادة التوجيه إلى صفحة تسجيل الدخول

if __name__ == '__main__':
    app.run(debug=True)

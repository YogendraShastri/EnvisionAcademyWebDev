from flask import Flask, session, redirect
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql
from datetime import datetime
from flask_mail import Mail
from slugify import slugify
import builtins
import os
import math
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

builtins.unicode=str
ALLOWED_EXTENSIONS={'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

pymysql.install_as_MySQLdb()
with open('config.json', 'r') as c:
    params=json.load(c)['params']

local_server=True

app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=params['Gmail-user']
app.config['MAIL_PASSWORD']=params['Gmail-password']
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['UPLOAD_FOLDER']='D:\myprojects\static\img'
mail=Mail(app)
app.secret_key='thisismysecretkey'

if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"]=params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"]=params['prod_uri']
db=SQLAlchemy(app)


class contact_me(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), unique=False, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    phone=db.Column(db.String(50), unique=True, nullable=False)
    msg=db.Column(db.String(200), unique=False, nullable=False)
    date=datetime.now()


# class posts(db.Model):
#   sno = db.Column(db.Integer, primary_key=True)
#  title = db.Column(db.String(50), unique=False, nullable=False)
# slug = db.Column(db.String(21), unique=True, nullable=False)
# content = db.Column(db.String(200), unique=False, nullable=False)
# date = db.Column(db.String(12), unique=False, nullable=False)


class posts(db.Model):
    # __tablename__ = "posts"
    sno=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(50), unique=False, nullable=False)
    slug=db.Column(db.String(21), unique=True, nullable=False)
    content=db.Column(db.String(200), unique=False, nullable=False)
    date=datetime.now()
    img_file=db.Column(db.String(26), unique=False, nullable=False)

    # def __init__(self, slug, content, title, date, img_file):
    #   self.title = title
    #  self.content = content
    # self.slug = slugify(slug)
    # self.date = date
    # self.img_file = img_file


class video_tutorials(db.Model):
    # __tablename__ = "posts"
    sno=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(50), unique=False, nullable=False)
    description=db.Column(db.String(200), unique=True, nullable=False)
    link=db.Column(db.String(100), unique=False, nullable=False)


class faculty(db.Model):
    # __tablename__ = "posts"
    sno=db.Column(db.Integer, primary_key=True, autoincrement=True)
    image=db.Column(db.String(20), unique=False, nullable=True)
    name=db.Column(db.String(20), unique=False, nullable=False)
    details=db.Column(db.String(200), unique=True, nullable=False)
    phone=db.Column(db.String(20), unique=False, nullable=False)


class courses(db.Model):
    # __tablename__ = "posts"
    sno=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(20), unique=False, nullable=False)
    description=db.Column(db.String(200), unique=True, nullable=False)
    date=datetime.now()


@app.route('/')
def home():
    post=posts.query.all()
    course= courses.query.all()
    # last=math.ceil(len(post) / int(params['number_of_posts']))
    # page=request.args.get('page', 1, type=int)
    # if (not str(page).isnumeric()):
    #     page=1
    # post=post[(page - 1) * int(params['number_of_posts']):(page - 1) * int(params['number_of_posts']) + int(
    #     params['number_of_posts'])]
    # if page == 1:
    #     prev="#"
    #     next="/?page=" + str(page + 1)
    # elif page == last:
    #     prev="/?page=" + str(page - 1)
    #     next="#"
    # else:
    #     prev="/?page=" + str(page - 1)
    #     next="/?page=" + str(page + 1)
    return render_template('index.html', params=params, posts=post, courses=course)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_login']:
        post=posts.query.all()
        return render_template('dashboard.html', params=params, posts=post)

    if request.method == 'POST':
        username=request.form.get('uname')
        userpass=request.form.get('upass')
        if username == params['admin_login'] and userpass == params['admin_password']:
            # set the session
            session['user']=username
            post=posts.query.all()
            return render_template('dashboard.html', params=params, posts=post)

    return render_template('login.html', params=params)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name_v=request.form.get('name')
        email_v=request.form.get('email')
        phone_v=request.form.get('phone')
        msg_v=request.form.get('message')
        entry_v=contact_me(name=name_v, phone=phone_v, email=email_v, msg=msg_v)
        db.session.add(entry_v)
        db.session.commit()
        mail.send_message(
            'new blog message by' + name_v,
            sender=email_v,
            recipients=[params['Gmail-user']],
            body=msg_v + '\n' + phone_v
        )
    return render_template('contact.html', params=params)


# @app.route("/pos/<posts_slug>", methods=['GET', 'POST'])
# def post_route(posts_slug):
#   post = db.session.query(posts).filter_by(slug=posts_slug).one()
#  return render_template('post.html', params=params, post=post)

@app.route('/posts/<slug>', methods=['GET', 'POST'])
def show(slug):
    post=posts.query.filter_by(slug=slug).first()
    if post:
        return render_template("post.html", posts=post, params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            box_title_v=request.form.get('title')
            slug_v=request.form.get('slug')
            content_v=request.form.get('content')
            img_file_v=request.form.get('img_file')
            date_v=datetime.now()
            if sno == '0':
                post_v=posts(title=box_title_v, slug=slug_v, content=content_v, img_file=img_file_v, date=date_v)
                db.session.add(post_v)
                db.session.commit()
            else:
                post=posts.query.filter_by(sno=sno).first()
                post.title=box_title_v
                post.slug=slug_v
                post.content=content_v
                post.img_file=img_file_v
                post.date=date_v
                db.session.commit()
                return redirect('/edit/' + sno)
    post=posts.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, sno=sno, post=post)


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            file1=request.files['file1']
            path=os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file1.filename))
            file1.save(path)
            return "uploaded successfully"


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/delete/<string:sno>', methods=['GET', 'POST'])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        post=posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


@app.route("/add_videos", methods=['GET', 'POST'])
def add_videos():
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            video_title_v=request.form.get('title')
            video_desc=request.form.get('desc')
            video_link=request.form.get('link')
            post_v=video_tutorials(title=video_title_v, description=video_desc, link=video_link)
            db.session.add(post_v)
            db.session.commit()
    video_tutorial=video_tutorials.query.all()
    return render_template('add_videos.html', params=params, video_tutorial=video_tutorial)


@app.route("/edit_videos/<string:sno>", methods=['GET', 'POST'])
def add_videos2(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            video_title_v=request.form.get('title')
            video_desc=request.form.get('desc')
            video_link=request.form.get('link')
            post=video_tutorials.query.filter_by(sno=sno).first()
            post.title=video_title_v
            post.description=video_desc
            post.link=video_link
            db.session.commit()
            return redirect('/edit_videos/' + sno)
    post=video_tutorials.query.filter_by(sno=sno).first()
    return render_template('edit_videos.html', params=params, sno=sno, post=post)


@app.route('/delete_videos/<string:sno>', methods=['GET', 'POST'])
def delete_videos(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        video_tutorial=video_tutorials.query.filter_by(sno=sno).first()
        db.session.delete(video_tutorial)
        db.session.commit()
    return redirect('/dashboard')


@app.route('/videos')
def videos():
    video_tutorial=video_tutorials.query.all()
    return render_template('videos.html', params=params, video_tutorial=video_tutorial)


@app.route("/add_faculty", methods=['GET', 'POST'])
def add_faculty():
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            faculty_image=request.form.get('image')
            faculty_title_v=request.form.get('name')
            faculty_desc=request.form.get('details')
            faculty_phone=request.form.get('phone')
            post_v=faculty(image=faculty_image, name=faculty_title_v, details=faculty_desc, phone=faculty_phone)
            db.session.add(post_v)
            db.session.commit()
    faculty_v=faculty.query.all()
    return render_template('add_faculty.html', params=params, faculty=faculty_v)


@app.route('/notice')
def notice_board():
    faculty_v=faculty.query.all()
    return render_template('notic_borad.html', params=params, posts=faculty_v)


@app.route("/edit_faculty/<string:sno>", methods=['GET', 'POST'])
def add_faculty2(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            faculty_img=request.form.get('image')
            faculty_title_v=request.form.get('name')
            faculty_desc=request.form.get('details')
            faculty_phone=request.form.get('phone')
            faculty_v=faculty.query.filter_by(sno=sno).first()
            faculty_v.image=faculty_img
            faculty_v.name=faculty_title_v
            faculty_v.details=faculty_desc
            faculty_v.phone=faculty_phone
            db.session.commit()
            return redirect('/edit_faculty/' + sno)
    faculty_v=faculty.query.filter_by(sno=sno).first()
    return render_template('edit_faculty.html', params=params, sno=sno, post=faculty_v)


@app.route('/delete_faculty/<string:sno>', methods=['GET', 'POST'])
def delete_faculty(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        faculty_v=faculty.query.filter_by(sno=sno).first()
        db.session.delete(faculty_v)
        db.session.commit()
    return redirect('/dashboard')


@app.route("/add_courses", methods=['GET', 'POST'])
def add_courses():
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            courses_title_v=request.form.get('title')
            courses_desc=request.form.get('desc')
            courses_date=datetime.now()
            post_v=courses(title=courses_title_v, description=courses_desc, date=courses_date)
            db.session.add(post_v)
            db.session.commit()
    courses_v=courses.query.all()
    return render_template('courses.html', params=params, courses=courses_v)



@app.route("/edit_courses/<string:sno>", methods=['GET', 'POST'])
def edit_courses(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        if request.method == 'POST':
            courses_title_v=request.form.get('title')
            courses_desc=request.form.get('desc')
            courses_v=courses.query.filter_by(sno=sno).first()
            courses_v.title=courses_title_v
            courses_v.description=courses_desc
            db.session.commit()
            return redirect('/edit_courses/' + sno)
    courses_v=courses.query.filter_by(sno=sno).first()
    return render_template('edit_courses.html', params=params, sno=sno, post=courses_v)

@app.route('/delete_courses/<string:sno>', methods=['GET', 'POST'])
def delete_courses(sno):
    if 'user' in session and session['user'] == params['admin_login']:
        courses_v=courses.query.filter_by(sno=sno).first()
        db.session.delete(courses_v)
        db.session.commit()
    return redirect('/dashboard')


app.run(debug=True)

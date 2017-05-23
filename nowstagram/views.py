# -*- encoding=utf-8 -*-

from nowstagram import app,db
from flask import  render_template,redirect,request,flash,get_flashed_messages
from models import Image,User,Comment
import random,hashlib


@app.route('/')
def index():
    images = Image.query.order_by('id desc').limit(10).all()
    return render_template('index.html',images = images)

@app.route('/image/<int:image_id>/')
def image(image_id):
    image = Image.query.get(image_id)
    if image == None:
        return  redirect('/')
    return render_template('pageDetail.html', image = image)


@app.route('/profile/<int:user_id>/')
def profile(user_id):
    user = User.query.get(user_id)
    if user == None:
        return  redirect('/')
    return render_template('profile.html', user = user)


@app.route('/regloginpage/')
def regloginpage():
    msg = ''
    for m in get_flashed_messages(with_categories=False,category_filter=['reglogin']):
        msg = msg + m
    return render_template('login.html',msg=msg)

def reredirect_with_msg(target, msg, category):
    if msg != None:
        flash(msg, category=category)
    return redirect(target)

@app.route('/reg/',methods={'post','get'})
def reg():

    username = request.values.get('username').strip()
    password = request.values.get('password').strip()

    user = User.query.filter_by(username=username).first()

    if username == '' or password == '':
        return reredirect_with_msg('/regloginpage/', u'用户名和密码不能为空', 'reglogin')

    if user != None:
        return reredirect_with_msg('/regloginpage/',u'用户名已存在','reglogin')
    ##更多判断

    salt = '.'.join(random.sample('abcdefgaop46445',5))
    m = hashlib.md5()
    m.update(password+salt)
    password = m.hexdigest()
    user = User(username,password,salt)
    db.session.add(user)
    db.session.commit()

    return redirect('/')


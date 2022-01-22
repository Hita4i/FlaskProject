from flask import Flask, render_template, request, redirect, url_for, flash
from base import app, db, User, Equip
from werkzeug.security import generate_password_hash, check_password_hash

users = ['user1', 'user2',
         'user3', 'user4',
         'user5', 'user6',
         'user7', 'user8', ]


def index():
    return render_template('index.html')


def login():
    return render_template('login.html')


def about_equip(id):
    equip_list = Equip.query.get(id)
    return render_template('about_equip.html', equip_list=equip_list)


def del_equip(id):
    equip_list = Equip.query.get_or_404(id)
    try:
        db.session.delete(equip_list)
        db.session.commit()
        return view_equip()
    except:
        return 'Ошибка удаления'


def reg():
    if request.method == 'POST':
        if len(request.form.get('name')) > 4 and \
                len(request.form.get('email')) > 5 and \
                len(request.form.get('psw')) > 4 and \
                len(request.form.get('psw2')) > 4 \
                and request.form.get('psw') == request.form.get('psw2'):
            pasw_hash = generate_password_hash(request.form.get('psw'))
            name = request.form.get('name')
            email = request.form.get('email')
            new_user = User(username=name,
                            email=email,
                            password=pasw_hash)
            try:
                db.session.add(new_user)
                db.session.commit()
                return login()
            except:
                flash('Ошибка регистрации')
    else:
        return render_template('registration.html')


def view_equip():
    equip_list = Equip.query.all()

    return render_template('view_equip.html', equip_list=equip_list)


def edit_equip():
    if request.method == 'POST':
        equipment = request.form.get('equipment')
        equipment_number = request.form.get('equipment_number')
        user_id = request.form.get('user_id')
        new_equip = Equip(equipment=equipment,
                          equipment_number=equipment_number,
                          user_id=user_id)
        try:
            db.session.add(new_equip)
            db.session.commit()
            return view_equip()
        except:
            return 'Ошибка добавления'
    else:
        return render_template('edit_equip.html', users=users)

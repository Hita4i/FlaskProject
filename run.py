from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from base import db, User, Equip

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/edit_equip', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        equip = request.form.get('equip')
        equip_number = request.form.get('equip_number')
        user_id = request.form.get('user_id')
        n = Equip(equipment='DA', equipment_number=11)
        db.session.add(n)
        db.session.commit()
        return redirect('/')
    #     equip = request.form.get('equip')
    #     equip_number = request.form.get('equip_number')
    #     user_id = request.form.get('user_id')
    #     new_equip = Equip(equipment=equip,
    #                       equipment_number=equip_number)
    #     print(equip, equip_number, user_id)
    #     try:
    #         db.session.add(n)
    #         print('added')
    #         db.session.commit()
    #         print('oll ok')
    #         return redirect('/')
    #     except:
    #         print('Ошибка добавления')
    #         return redirect('/edit_equip.html')
    else:
        return render_template('/edit_equip.html')


if __name__ == '__main__':
    app.run(debug=True)
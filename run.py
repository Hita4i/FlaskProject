from flask import Flask, render_template, request, redirect
from base import app, db, User, Equip



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/edit_equip', methods=['POST', 'GET'])
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
            return redirect('/')
        except:
            return 'Ошибка добавления'
    else:
        return render_template('edit_equip.html')


def reed():
    pass

if __name__ == '__main__':
    app.run(debug=True)
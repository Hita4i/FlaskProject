from func import *
import func


@app.route('/')
@app.route('/index')
def index():
    return func.index()


@app.route('/login')
def login():
    return func.login()


@app.route('/about_equip/<int:id>')
def about_equip(id):
    return func.about_equip(id)


@app.route('/about_equip/<int:id>/del')
def del_equip(id):
    return func.del_equip(id)


@app.route('/edit_equip', methods=['POST', 'GET'])
def edit_equip():
    return func.edit_equip()


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    return func.reg()


@app.route('/view_equip')
def view_equip():
    return func.view_equip()


if __name__ == '__main__':
    app.run(debug=True)

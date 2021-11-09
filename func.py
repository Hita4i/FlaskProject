# from base import db, User, Equip
# from flask import Flask, render_template, url_for, redirect, request
#
#
# def edit_equip():
#     if request.method == 'POST':
#         equip = request.form.get('equip')
#         equip_number = request.form.get('equip_number')
#         user_id = request.form.get('user_id')
#         new_equip = Equip(equipment=equip,
#                           equipment_number=equip_number,
#                           user_id=user_id)
#         try:
#             db.session.add(new_equip)
#             db.session.commit()
#             print('oll ok')
#         except:
#             print('Ошибка добавления')
#             return redirect('/edit_equip.html')
#         finally:
#             render_template('edit_equip.html')
#

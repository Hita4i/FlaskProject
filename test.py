import werkzeug.security as wr


passw = '12345'


passw_hash = wr.generate_password_hash(passw)
psw_check = wr.check_password_hash(passw_hash, '12345')
print(passw_hash)
print(psw_check)
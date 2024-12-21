import sqlite3 as sq
global base, cur
def sql_start():
    global base, cur
    base = sq.connect('shop.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS clot(img TEXT, name TEXT, size TEXT, quantity TEXT, ids TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS acses(img TEXT, name TEXT, size TEXT, quantity TEXT, ids TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS obyv(img TEXT, name TEXT, size TEXT, quantity TEXT, ids TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS zakazy(user TEXT, img TEXT, name TEXT, size TEXT, quantity TEXT, ids TEXT, check_status TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS admins(admin_id TEXT)')
    base.commit()
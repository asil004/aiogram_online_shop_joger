import sqlite3 as sq

db = sq.connect('tg.db')
cr = db.cursor()


async def db_start():
    cr.execute("CREATE TABLE IF NOT EXISTS accounts("
               "id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "tg_id INTEGER,"
               "cart_id TEXT)")
    cr.execute("CREATE TABLE IF NOT EXISTS items("
               "i_id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "name TEXT,"
               "desc TEXT, "
               "price TEXT, "
               "photo TEXT, "
               "brand TEXT)")
    db.commit()


async def cm_db_start(user_id):
    user = cr.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cr.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()

import sqlite3
import random
from django.contrib.auth.hashers import make_password

path = r'E:\\MyGit\\Wallpaper_Website\\wallpaper\\db.sqlite3'


def init_category():
    con = sqlite3.connect(path)
    cur = con.cursor()
    clear_sql = "delete from db_category"
    print(clear_sql)
    cur.execute(clear_sql)
    con.commit()

    for i in range(30):
        sqlite_insert = ("insert into db_category('name','count') values('{0}','{1}')"
                         .format('category_' + str(i), random.randint(10, 500)))
        print(sqlite_insert)
        cur.execute(sqlite_insert)
    con.commit()
    con.close()


def init_tag():
    con = sqlite3.connect(path)
    cur = con.cursor()
    clear_sql = "delete from db_tag"
    print(clear_sql)
    cur.execute(clear_sql)
    con.commit()

    for i in range(300):
        sqlite_insert = ("insert into db_tag('name','count') values('{0}','{1}')"
                         .format('tag_' + str(i), random.randint(10, 500)))
        print(sqlite_insert)
        cur.execute(sqlite_insert)
    con.commit()
    con.close()


init_category()
init_tag()




# createsuperuser
#
# user_admin
#
# user_admin@email.com
#
# qwer1234
#
# qwer1234

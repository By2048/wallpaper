import sqlite3
import random
import pymysql

from django.contrib.auth.hashers import make_password



def init_category():
    db = pymysql.connect("localhost", "root", "mysql_password", "wallpaper")
    cur = db.cursor()
    clear_sql = "delete from db_image_category"
    print(clear_sql)
    cur.execute(clear_sql)
    db.commit()

    for i in range(30):
        sqlite_insert = ("insert into db_image_category(name,count) values('{0}',{1})"
                         .format('category_' + str(i), random.randint(10, 500)))
        print(sqlite_insert)
        cur.execute(sqlite_insert)
    db.commit()
    db.close()


def init_tag():
    db = pymysql.connect("localhost", "root", "mysql_password", "wallpaper")
    cur = db.cursor()
    clear_sql = "delete from db_image_tag"
    print(clear_sql)
    cur.execute(clear_sql)
    db.commit()

    for i in range(500):
        sqlite_insert = ("insert into db_image_tag(name,count) values('{0}',{1})"
                         .format('tag_' + str(i), random.randint(10, 500)))
        print(sqlite_insert)
        cur.execute(sqlite_insert)
    db.commit()
    db.close()


if __name__ == '__main__':
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

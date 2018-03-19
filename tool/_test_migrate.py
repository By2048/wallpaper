import sqlite3
import os

wallpaper_path = 'E:\\MyGit\\Wallpaper_Website\\wallpaper\\app'

def del_all_migrations():
    for app in os.listdir(wallpaper_path):
        migrations_path = os.path.join(wallpaper_path, app, 'migrations')
        for initial_file in os.listdir(migrations_path):
            if initial_file in ['__init__.py', '__pycache__']:
                pass
            else:
                sql_init_file = os.path.join(migrations_path, initial_file)
                print(sql_init_file)
                os.remove(sql_init_file)


del_all_migrations()


def clear_sql():
    pass


# str = "[www.runoob.com]"
#
# print ("str.center(40, '*') : ", str.center(40, ' '))
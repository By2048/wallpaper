import sqlite3
import os

wallpaper_path = 'E:\\MyGit\\Wallpaper_Website\\app'


def del_all_migrations():
    for app in os.listdir(wallpaper_path):
        migrations_path = os.path.join(wallpaper_path, app, 'migrations')
        if os.path.exists(migrations_path):
            for initial_file in os.listdir(migrations_path):
                if initial_file in ['__init__.py', '__pycache__']:
                    pass
                else:
                    sql_init_file = os.path.join(migrations_path, initial_file)
                    print(sql_init_file)
                    os.remove(sql_init_file)
        else:
            pass

del_all_migrations()

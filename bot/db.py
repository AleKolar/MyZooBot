import sqlite3

from typing import TYPE_CHECKING

#if TYPE_CHECKING:
    #from handlers.try_choosing_handlers import amount


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exist(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM 'photos' WHERE 'user_id' = ?", (user_id,)).fetchall()
            #return bool(len(res))
            if bool(len(res)) == False:
                result = self.cursor.execute("SELECT * FROM 'photos' WHERE 'user_id' = ?", (user_id,))
                print(result)
                for p in result:
                    with open(f'{'amount_user'}.jpeg', 'wb') as file:
                        return file.write(p[0])
            else:
                return bool(len(res))


    def add_pic(self, user_id, amount):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS photos(user_id INTEGER PRIMARY KEY, photo BLOB, amount_user INTEGER)')
        for i in range(13, 22):
            if i == amount:
                with open(f'{i}.jpeg', 'rb') as photo:
                    h = photo.read()
                    #self.cursor.execute('INSERT INTO photos(photo) VALUES(?)', [h])
                    self.cursor.execute("INSERT INTO photos (photo, amount_user, user_id) VALUES (?, ?, ?)", (h, f'{i}.jpeg', user_id))
                    return self.connection.commit()


    def get_photo(self, user_id):
        photo = self.cursor.execute("SELECT photo FROM photos WHERE user_id = amount_user")
        for amount in photo:
            with open(f'{amount}.jpeg', 'wb') as file:
                return file.write(amount[0])







import sqlite3
#from PIL import Image
#from typing import TYPE_CHECKING




#if TYPE_CHECKING:
    #from handlers.try_choosing_handlers import amount


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exist(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM photos WHERE user_id = ?", (user_id,)).fetchall()
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
        '''
        photo = self.cursor.execute("SELECT photo FROM photos WHERE user_id = user_id").fetchone()
        for p in photo:
            with open(f'{user_id}.jpeg', 'wb') as file:
                io_bytes = io.BytesIO(p)
                img = Image.open(io_bytes)
                return img
                img.show()
        '''

        photo = self.cursor.execute("SELECT photo FROM photos WHERE user_id = user_id").fetchone()
        for p in photo:
            image_data = photo[0]
            with open(f'{user_id}.jpeg', 'wb') as file:
                file.write(image_data)
                return f'{user_id}.jpeg'
                #return img.show()
                #return file.write(image_data)
#


    def close(self):
        self.connection.close()


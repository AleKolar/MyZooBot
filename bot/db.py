import io
import sqlite3

from typing import TYPE_CHECKING

from PIL import Image, ImageFont

if TYPE_CHECKING:
    from handlers.try_choosing_handlers import amount

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()



    def user_exist(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM 'photos' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(res))

    '''def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'photos' ('user_id') VALUES (?)", (user_id,))
            return self.connection.commit()'''

    def add_pic(self, user_id):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS photos(user_id INTEGER PRIMARY KEY, photo BLOB, amount_user INTEGER)')
        amount = 13
        for i in range(13, 22):
            with open(f'{i}.jpeg', 'rb') as photo:
                    h = photo.read()
                    #self.cursor.execute('INSERT INTO photos(photo) VALUES(?)', [h])
                    self.cursor.execute("INSERT INTO photos (photo, amount_user, user_id) VALUES (?, ?, ?)", (h, f'{i}.jpeg', user_id))
                    print(h, f'{i}.jpeg', user_id)
                    return self.connection.commit()


    def get_photo(self, user_id):
        '''self.cursor.execute("SELECT photo FROM photos WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()
        result_pass = None
        if result is not None:
            result_pass = result[0]
            return result_pass
        '''
        result = self.cursor.execute("SELECT photo FROM photos WHERE user_id=?", (user_id,))
        amount = 13
        for p in result:
            with open(f'{amount}.jpeg', 'wb') as file:
                return file.write(p[0])

        '''img = Image.open(f'{amount}.jpeg')
        print(img)
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=75)

            # You probably want
        desiredObject = buffer.getbuffer()
        print(desiredObject)'''


    def close(self):
        self.connection.close()



a = Database('DB1')
#print(a.add_pic(111))
print(a.get_photo(111))

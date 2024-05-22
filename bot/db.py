import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def user_exist(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(res))

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
            return self.connection.commit()

    def add_pic(self):
        self.cursor.execute('CREATE TABLE IF NOT EXIST photos(amount_photo INTEGER PRIMARY KEY, photo BLOB)')
        for i in range(1, 10):
            with open(f'{i}.jpeg', 'rb') as photo:
                h = photo.read()
                self.cursor.execute('INSERT INTO photos(photo) VALUES(?)', [h])
                return self.connection.commit()

    def close(self):
        self.connection.close()





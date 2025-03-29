import psycopg2

from Postgresql.postgresql_config import host, user, password, db_name


class DB:
    def __init__(self):
        self.connection = psycopg2.connect(host=host,
                                           user=user,
                                           password=password,
                                           database=db_name)
        self.cursor = self.connection.cursor()


    def postgre_conn(self):
        try:
            # connect to exist database
            self.sconnection.autocommit = True

            # the cursor for perfoming database operations
            # cursor = connection.cursor()

            with self.cursor as cursor:
                cursor.execute(
                    "SELECT version();"
                )

                print(f"Server version: {cursor.fetchone()}")
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if self.connection:
                # cursor.close()
                self.connection.close()
                print("[INFO] PostgreSQL connection closed")

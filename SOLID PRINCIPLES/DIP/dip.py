class DatabaseInterface:
    def query(self, sql):
        raise NotImplementedError

class MySQLDatabase(DatabaseInterface):
    def __init__(self, host, username, password, database):
        self.connection = mysql.connect(host=host, user=username, password=password, database=database)

    def query(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

class PostgreSQLDatabase(DatabaseInterface):
    def __init__(self, host, username, password, database):
        self.connection = psycopg2.connect(host=host, user=username, password=password, database=database)

    def query(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

class User:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    def save(self):
        self.database.query("INSERT INTO users (username, password) VALUES ('john.doe', 'password')")
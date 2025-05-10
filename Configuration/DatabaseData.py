import pyodbc as db 

class DatabaseData:
    """Class to connect to database and fetch data"""
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def get_connection_string(self):
        """Get coneecntion string method"""
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"

    def connect(self):
        """data base coneection Method"""
        connection_string = self.get_connection_string()
        try:
            connection = db.connect(connection_string)
            return connection
        except db.Error as e:
            print(f"Error connecting to database: {e}")
            return None
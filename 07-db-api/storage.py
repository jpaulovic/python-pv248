import sqlite3


class TemperatureStorage:
    def __init__(self, fname='temperatures.db'):
        """Temperature storage"""
        self.db = sqlite3.connect(fname)
        self._setup_tables()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    def _setup_tables(self):
        """Create table when needed"""
        query = """
                CREATE TABLE IF NOT EXISTS notes( 
                    timestamp int primary key, 
                    value float
                );"""
        c = self.db.cursor()
        c.execute(query)
        self.db.commit()

    def put_value(self, timestamp, value):
        """put some measurement inside"""
        existing = self.get_value(timestamp)
        if not existing:
            query = "INSERT INTO notes VALUES ('{}','{}');".format(timestamp,value)
            c = self.db.cursor()
            c.execute(query)
            self.db.commit()

    def get_value(self, timestamp):
        """get some measurement inside"""
        query = "SELECT value FROM notes WHERE timestamp='{}'".format(
            timestamp)
        c = self.db.cursor()
        result = c.execute(query)
        return result.fetchone()

    def get_latest_value(self):
        """return latest value"""
        query = "SELECT value FROM notes ORDER BY timestamp DESC LIMIT 1;"
        c = self.db.cursor()
        result = c.execute(query)
        return result.fetchone()

    def get_all_values(self):
        """return all entries in database ordered by timestamp"""
        query = "SELECT * FROM notes ORDER BY timestamp DESC"
        c = self.db.cursor()
        result = c.execute(query)
        return result.fetchall()

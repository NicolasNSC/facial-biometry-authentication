from multiprocessing import connection
import mysql.connector
from mysql.connector import Error


class DatabaseConnector:
    '''The class responsible to connect the application with the database.'''
    
    def __init__(self, host:str, user:str, password, database_name:str):
        self._host = host
        self.user = user
        self.password = password
        self._database_name = database_name
        
        self.query = None
        self.connection = None
        
        
    def create_connection(self):
        '''Stabilishes a connection with the database.'''
        
        try:
            self.connection = mysql.connector.connect(
                host = self._host,
                user = self.user,
                passwd = self.password,
                database = self._database_name,
            )
            print("MySQL Database connection successfull!")
        except Error:
            print(f"Error: {Error}")
            
        return self.connection


    def create_database(self):
        '''Create a database.'''
        cursor = connection.cursor()
        
        try:
            cursor.execute(self.query)
            print("Database created successfully!")
        except Error:
            print(f"Error: {Error}")


    def execute_query(self):
        '''Executes a query.'''
        cursor = connection.cursor()
        
        try:
            cursor.execute(self.query)
            connection.commit()
            print("Query successfull!")
        except Error:
            print(f"Error: {Error}")
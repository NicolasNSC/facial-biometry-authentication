from dataController import DatabaseConnector

connection = DatabaseConnector(host="localhost", user="host", password="password", database_name="database")
connection.create_connection()
connection.execute_query()

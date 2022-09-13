from dataController import DatabaseConnector


connection = DatabaseConnector(host="localhost", user="host", password="password", database_name="database")

#create_database_query = "CREATE DATABASE school"
#create_database(connection, create_database_query)
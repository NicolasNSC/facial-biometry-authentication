from dataController import create_database, create_db_connection


pssword = "" 
connection = create_db_connection("localhost", "host", pssword, "database")
#create_database_query = "CREATE DATABASE school"
#create_database(connection, create_database_query)
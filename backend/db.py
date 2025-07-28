import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",  # Replace with your MySQL password
        database="ecommerce_db"
    )


import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # or your MySQL username
        password="Ravi@1818",   # replace with your MySQL password
        database="portfolio_db"
    )

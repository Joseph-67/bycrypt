"""
Database connection handler
Provides MySQL connection with DictCursor for easy row access
"""
import pymysql

def get_db_connection():
    """Returns a MySQL connection with DictCursor"""
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='flask_auth',
        cursorclass=pymysql.cursors.DictCursor
    )

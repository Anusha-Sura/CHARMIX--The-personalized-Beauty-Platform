import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="141.209.241.57",
        user="sura1a",         
        password="mypass", 
        database="BIS698Fall25_47"
    )

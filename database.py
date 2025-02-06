# database.py
import psycopg2

# Configuración de la conexión a PostgreSQL
def get_db_connection():
    """get connection"""
    return psycopg2.connect(
        host="98.84.245.136",
        database="items",
        user="stalin",
        password="stalin"
    )
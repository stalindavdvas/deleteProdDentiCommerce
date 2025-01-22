from flask import Flask, jsonify
import psycopg2
from psycopg2 import sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuración de la conexión a PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host="host.docker.internal",  # Para conectar con PostgreSQL desde Docker
        database="items",             # Nombre de la base de datos
        user="postgres",              # Usuario de PostgreSQL
        password="stalin"             # Contraseña de PostgreSQL
    )

@app.route('/productos/<int:product_id>', methods=['DELETE'])
def eliminar_producto(product_id):
    """Eliminar un producto por su ID"""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Eliminar el producto por ID
        query = """
            DELETE FROM products
            WHERE id = %s
            RETURNING id;
        """
        cursor.execute(query, (product_id,))
        eliminado = cursor.fetchone()

        if not eliminado:
            return jsonify({'error': 'Producto no encontrado'}), 404

        conn.commit()
        return jsonify({'message': f'Producto con ID {eliminado[0]} eliminado exitosamente'}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Bloque __main__ para ejecutar el microservicio en el puerto 5004
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)

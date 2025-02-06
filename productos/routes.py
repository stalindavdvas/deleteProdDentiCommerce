# productos/routes.py
from . import productos_bp
from flask import jsonify
from database import get_db_connection

# Register DELETE /products/<int:product_id> in Blueprint
@productos_bp.route('/<int:product_id>', methods=['DELETE'])
def eliminar_producto(product_id):
    """delete id"""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # delete by id
        query = """
            DELETE FROM products
            WHERE id = %s
            RETURNING id;
        """
        cursor.execute(query, (product_id,))
        eliminado = cursor.fetchone()

        if not eliminado:
            return jsonify({'error': 'Product not found'}), 404

        conn.commit()
        return jsonify({'message': f'Product with ID {eliminado[0]} delete sucessfull'}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()
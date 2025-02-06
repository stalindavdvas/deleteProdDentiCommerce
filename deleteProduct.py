# app.py
from flask import Flask
from flask_cors import CORS
from productos import productos_bp  # Importar el Blueprint de productos

app = Flask(__name__)
CORS(app)

# Registrar el Blueprint de productos con el prefijo '/productos'
app.register_blueprint(productos_bp, url_prefix='/productos')

# Bloque __main__ para ejecutar el microservicio en el puerto 5004
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, jsonify  # Adicionando jsonify aqui
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret key
jwt = JWTManager(app)

# Import routes here
from routes import user_routes, department_routes, ticket_routes
from tickets.urls import tickets  # Importing tickets module
from routes.status_routes import status_routes  # Importando status_routes separadamente

app.register_blueprint(user_routes)
app.register_blueprint(department_routes)
app.register_blueprint(ticket_routes)
app.register_blueprint(tickets)  # Registrando tickets module
app.register_blueprint(status_routes)  # Registrando status_routes

@app.route('/routes', methods=['GET'])
def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(str(rule))
    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from models import db, Client  # Assuming SQLAlchemy is used for database management

app = Flask(__name__)

@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    new_client = Client(
        name=data['name'],
        id_number=data['id_number'],
        mobile_number=data['mobile_number'],
        residence=data['residence'],
        business_type=data['business_type'],
        business_location=data['business_location']
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Client added successfully!'}), 201

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    clients_list = [{"id": c.id, "name": c.name, "id_number": c.id_number} for c in clients]
    return jsonify(clients_list), 200
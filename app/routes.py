from flask import Blueprint, request, jsonify
from app.models import db, Client, Loan, Transaction

routes = Blueprint('routes', __name__)

@routes.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    client = Client(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(client)
    db.session.commit()
    return jsonify({"message": "Client created successfully"}), 201

@routes.route('/loans', methods=['POST'])
def create_loan():
    data = request.json
    loan = Loan(client_id=data['client_id'], amount=data['amount'], interest_rate=data['interest_rate'])
    db.session.add(loan)
    db.session.commit()
    return jsonify({"message": "Loan created successfully"}), 201
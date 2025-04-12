from flask import Flask, request, jsonify
from models import db, Loan, Payment

app = Flask(__name__)

@app.route('/loans', methods=['POST'])
def create_loan():
    data = request.get_json()
    new_loan = Loan(
        client_id=data['client_id'],
        loan_amount=data['loan_amount'],
        interest_rate=8,
        appraisal_fee=300 if data['distance'] <= 5 else data['appraisal_fee'],
        start_date=data['start_date'],
        due_date=data['due_date'],
        principal_balance=data['loan_amount']
    )
    db.session.add(new_loan)
    db.session.commit()
    return jsonify({'message': 'Loan created successfully!'}), 201

@app.route('/loans/<int:loan_id>/repayment', methods=['POST'])
def make_payment(loan_id):
    data = request.get_json()
    loan = Loan.query.get_or_404(loan_id)

    payment = Payment(
        loan_id=loan.id,
        payment_date=data['payment_date'],
        amount_paid=data['amount_paid'],
        payment_type=data['payment_type']
    )
    db.session.add(payment)

    # Update loan balance
    if data['payment_type'] == 'principal':
        loan.principal_balance -= data['amount_paid']
    db.session.commit()
    return jsonify({'message': 'Payment recorded successfully!'}), 200
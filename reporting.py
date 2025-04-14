from flask import Flask, jsonify
from models import db, Loan, Client
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/reports/daily', methods=['GET'])
def daily_report():
    today = datetime.utcnow().date()
    loans = Loan.query.filter(Loan.start_date == today).all()
    report = [{"loan_id": l.id, "client_id": l.client_id, "amount": l.loan_amount} for l in loans]
    return jsonify(report), 200

@app.route('/reports/projections', methods=['GET'])
def weekly_projections():
    start_date = datetime.utcnow().date()
    end_date = start_date + timedelta(days=7)
    loans = Loan.query.filter(Loan.due_date.between(start_date, end_date)).all()
    projection = [{"loan_id": l.id, "amount_due": l.principal_balance * 1.08} for l in loans]
    return jsonify(projection), 200
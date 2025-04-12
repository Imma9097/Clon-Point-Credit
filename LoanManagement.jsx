import React, { useState, useEffect } from "react";
import axios from "axios";

const LoanManagement = () => {
  const [loans, setLoans] = useState([]);
  const [newLoan, setNewLoan] = useState({
    client_id: "",
    loan_amount: "",
    distance: "",
    start_date: "",
    due_date: "",
  });

  useEffect(() => {
    axios.get("/loans").then((response) => {
      setLoans(response.data);
    });
  }, []);

  const handleChange = (e) => {
    setNewLoan({ ...newLoan, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("/loans", newLoan).then(() => {
      alert("Loan created successfully!");
      setNewLoan({
        client_id: "",
        loan_amount: "",
        distance: "",
        start_date: "",
        due_date: "",
      });
    });
  };

  return (
    <div>
      <h1>Loan Management</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Client ID</label>
          <input
            type="text"
            className="form-control"
            name="client_id"
            value={newLoan.client_id}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Loan Amount</label>
          <input
            type="number"
            className="form-control"
            name="loan_amount"
            value={newLoan.loan_amount}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Create Loan
        </button>
      </form>
      <h2 className="mt-4">Loan List</h2>
      <ul>
        {loans.map((loan) => (
          <li key={loan.id}>Loan ID: {loan.id} - Amount: {loan.loan_amount}</li>
        ))}
      </ul>
    </div>
  );
};

export default LoanManagement;
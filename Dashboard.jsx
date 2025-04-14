import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [clients, setClients] = useState([]);
  const [loans, setLoans] = useState([]);

  useEffect(() => {
    // Fetch clients
    axios.get('/clients').then((response) => {
      setClients(response.data);
    });

    // Fetch loans
    axios.get('/loans').then((response) => {
      setLoans(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Clon Point Credit Dashboard</h1>
      <h2>Clients</h2>
      <ul>
        {clients.map((client) => (
          <li key={client.id}>{client.name} - {client.id_number}</li>
        ))}
      </ul>

      <h2>Loans</h2>
      <ul>
        {loans.map((loan) => (
          <li key={loan.id}>Loan ID: {loan.id} - Amount: {loan.loan_amount}</li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
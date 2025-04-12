import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const Reports = () => {
  const [projections, setProjections] = useState([]);

  useEffect(() => {
    axios.get('/reports/projections').then((response) => {
      setProjections(response.data);
    });
  }, []);

  const data = {
    labels: projections.map((p) => `Loan ID: ${p.loan_id}`),
    datasets: [
      {
        label: 'Weekly Projections',
        data: projections.map((p) => p.amount_due),
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 2,
      },
    ],
  };

  return (
    <div>
      <h1>Reports</h1>
      <Line data={data} />
    </div>
  );
};

export default Reports;
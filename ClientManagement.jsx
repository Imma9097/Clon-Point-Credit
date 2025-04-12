import React, { useState, useEffect } from "react";
import axios from "axios";

const ClientManagement = () => {
  const [clients, setClients] = useState([]);
  const [newClient, setNewClient] = useState({
    name: "",
    id_number: "",
    mobile_number: "",
    residence: "",
    business_type: "",
    business_location: "",
  });

  useEffect(() => {
    axios.get("/clients").then((response) => {
      setClients(response.data);
    });
  }, []);

  const handleChange = (e) => {
    setNewClient({ ...newClient, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("/clients", newClient).then(() => {
      alert("Client added successfully!");
      setNewClient({
        name: "",
        id_number: "",
        mobile_number: "",
        residence: "",
        business_type: "",
        business_location: "",
      });
    });
  };

  return (
    <div>
      <h1>Client Management</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Name</label>
          <input
            type="text"
            className="form-control"
            name="name"
            value={newClient.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">ID Number</label>
          <input
            type="text"
            className="form-control"
            name="id_number"
            value={newClient.id_number}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Mobile Number</label>
          <input
            type="text"
            className="form-control"
            name="mobile_number"
            value={newClient.mobile_number}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Add Client
        </button>
      </form>
      <h2 className="mt-4">Client List</h2>
      <ul>
        {clients.map((client) => (
          <li key={client.id}>{client.name} - {client.id_number}</li>
        ))}
      </ul>
    </div>
  );
};

export default ClientManagement;
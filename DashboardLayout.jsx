import React from "react";
import { Link } from "react-router-dom";

const DashboardLayout = ({ children }) => {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            Clon Point Credit
          </Link>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/clients">Clients</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/loans">Loans</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/reports">Reports</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container mt-4">{children}</div>
    </div>
  );
};

export default DashboardLayout;
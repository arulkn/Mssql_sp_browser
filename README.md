# MSSQL Stored Procedure Browser

Welcome to the **MSSQL Stored Procedure Browser**! This is a Python Flask application designed to help you analyze and manage SQL Server stored procedures efficiently. It provides a user-friendly interface to browse, filter, and analyze stored procedures, with features like highlighting keywords and tracking completed procedures.

---

## Features

- **Browse Stored Procedures**: View all stored procedures from your SQL Server database in a sidebar.
- **A-Z Filtering**: Filter stored procedures alphabetically using the A-Z filter in the sidebar.
- **Procedure Analysis**: Click on a stored procedure to view its definition and analyze it.
- **Keyword Highlighting**: Highlight specific keywords (e.g., `SELECT`, `FROM`) in the procedure definition for quick analysis.
- **Completion Tracking**: Mark procedures as "completed" and track them in a `completed_procedures.csv` file.
- **Dynamic Sidebar**: Once a procedure is marked as completed, it is removed from the sidebar.

---

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- PyODBC (for connecting to MSSQL)
- A SQL Server database

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arulkn/Mssql_sp_browser.git
   cd Mssql_sp_browser

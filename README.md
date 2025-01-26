# MSSQL Stored Procedure Browser

Welcome to the **MSSQL Stored Procedure Browser**! This is a Python Flask application designed to help you analyze and manage SQL Server stored procedures efficiently. It provides a user-friendly interface to browse, filter, and analyze stored procedures, with features like highlighting keywords and tracking completed procedures.

![image](https://github.com/user-attachments/assets/86601ca7-c94e-4c45-aabc-bb029053b70c)


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
2. **Install Dependencies**:
   Install the required Python packages using requirements.txt:

   ```bash
   
   pip install -r requirements.txt
   
3. **Configure the Database**:
   Create a db_config.json file in the root directory with your SQL Server connection details:

   ```json   
   {
     "server": "your-server-name",
     "database": "your-database-name",
     "username": "your-username",
     "password": "your-password"
   }

4. **Run the Application**:
   Start the Flask development server:

   ```bash
   python app.py

Open your browser and navigate to http://127.0.0.1:5000.

## Usage
**Browsing Stored Procedures**
 - The sidebar displays all stored procedures from your database.
 - Use the A-Z filter to narrow down the list of procedures.

**Analyzing a Procedure**
 - Click on a stored procedure to view its definition.
 - Use the Highlight feature to quickly locate keywords like SELECT, FROM, etc.:

   ```javascript
     highlightWordInClass('select', 'source');

**Marking a Procedure as Completed**
   - After analyzing a procedure, click the Complete button.
   - The procedure will be added to completed_procedures.csv and removed from the sidebar.

**File Structure**
      
      Mssql_sp_browser/
      ├── app.py                  # Main Flask application
      ├── database.py             # Database connection and stored procedure logic
      ├── db_config.json          # Database configuration file
      ├── requirements.txt        # Python dependencies
      ├── completed_procedures.csv # Tracks completed procedures
      ├── static/
      │   ├── js/
      │   │   └── script.js       # JavaScript for highlighting and UI interactions
      │   └── css/
      │       └── styles.css      # Custom styles
      └── templates/
          └── index.html          # Main HTML template

## Customization
**Database Configuration**
  - Modify db_config.json to connect to your SQL Server database.
           
**Stored Procedure Filtering**
  - To customize how stored procedures are filtered (e.g., removing prefixes like usp_), update the get_stored_procedures() function in database.py.
      
**Keyword Highlighting**
  - To highlight additional keywords, modify the highlightWordInClass() function in static/js/script.js.

## Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.

2. Create a new branch (git checkout -b feature/YourFeature).

3. Commit your changes (git commit -m 'Add some feature').

4. Push to the branch (git push origin feature/YourFeature).

5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Built with Python and Flask.

- Uses PyODBC for database connectivity.

- Inspired by the need for a simple tool to analyze SQL Server stored procedures.

 ---

Enjoy using the MSSQL Stored Procedure Browser! If you have any questions or feedback, feel free to open an issue or reach out.

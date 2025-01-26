import os  # Add this import
import csv
import pyodbc,textwrap
from config import load_config
from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import HtmlFormatter

def get_db_connection():
    config = load_config()

    # Build connection string based on authentication type
    if config.get('trusted_connection') == 'yes':
        conn_str = (
            f"DRIVER={{{config['driver']}}};"
            f"SERVER={config['server']};"
            f"DATABASE={config['database']};"
            "Trusted_Connection=yes;"
        )
    else:
        conn_str = (
            f"DRIVER={{{config['driver']}}};"
            f"SERVER={config['server']};"
            f"DATABASE={config['database']};"
            f"UID={config['username']};"
            f"PWD={config['password']};"
        )

    return pyodbc.connect(conn_str)

def test_connection(config):
    try:
        if config.get('trusted_connection') == 'yes':
            conn_str = (
                f"DRIVER={{{config['driver']}}};"
                f"SERVER={config['server']};"
                f"DATABASE={config['database']};"
                "Trusted_Connection=yes;"
            )
        else:
            conn_str = (
                f"DRIVER={{{config['driver']}}};"
                f"SERVER={config['server']};"
                f"DATABASE={config['database']};"
                f"UID={config['username']};"
                f"PWD={config['password']};"
            )

        conn = pyodbc.connect(conn_str)
        conn.close()
        return True, "Connection successful!"
    except pyodbc.Error as e:
        return False, f"Connection failed: {str(e)}"

def get_available_drivers():
    return [driver for driver in pyodbc.drivers() if 'SQL Server' in driver]

def get_stored_procedures():
    try:
        # Load completed procedures from the CSV file
        completed_procedures = set()
        if os.path.exists('completed_procedures.csv'):
            with open('completed_procedures.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    completed_procedures.add(row[0])  # Add procedure name to the set

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT OBJECT_SCHEMA_NAME(object_id) as schema_name,
               name as procedure_name
        FROM sys.procedures
        ORDER BY schema_name, procedure_name
        """

        cursor.execute(query)
        procedures = cursor.fetchall()

        # Filter out completed procedures
        display_names = []
        full_names = []
        for row in procedures:
            full_name = f"{row.schema_name}.{row.procedure_name}"
            if full_name not in completed_procedures:
                display_name = f"{row.schema_name}.{row.procedure_name.replace('usp_', '')}"
                display_names.append(display_name)
                full_names.append(full_name)

        cursor.close()
        conn.close()
        return display_names, full_names, None
    except Exception as e:
        return [], [], str(e)

def get_procedure_definition(procedure_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = f"""
        SELECT OBJECT_DEFINITION(OBJECT_ID('{procedure_name}')) as definition
        """

        cursor.execute(query)
        definition = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        # Ensure the definition has proper spaces (if not already)
        definition = definition.replace("\n", " ").replace("\t", " ")

        # Word wrap the definition to a maximum of 10 characters per line
        wrapped_definition = textwrap.fill(
            definition,
            width=130,
            break_long_words=False,  # Prevents splitting words
            replace_whitespace=False  # Preserves existing whitespace
        )

        # Highlight the SQL code
        formatted_code = highlight(
            wrapped_definition,
            SqlLexer(),
            HtmlFormatter(style='monokai', cssclass='source')
        )

        return formatted_code, None
    except Exception as e:
        return None, str(e)
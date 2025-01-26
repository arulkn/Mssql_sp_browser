from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import Token

# Custom style for SQL highlighting (optional)
class CustomSqlStyle(Style):
    styles = {
        Token.Keyword: 'bold #FF79C6',  # Pink for keywords
        Token.Name.Builtin: '#50FA7B',  # Green for built-in functions
        Token.String: '#F1FA8C',        # Yellow for strings
        Token.Comment: 'italic #6272A4',# Gray for comments
        Token.Operator: '#FF5555',      # Red for operators
        Token.Literal: '#BD93F9',       # Purple for literals
    }

def format_sql_code(sql_code, style='monokai', cssclass='source', linenos=False):
    """
    Formats MSSQL stored procedures or SQL code using Pygments.

    Args:
        sql_code (str): The SQL code to format.
        style (str): Pygments style to use (e.g., 'monokai', 'default').
        cssclass (str): CSS class for the HTML output.
        linenos (bool): Whether to include line numbers.

    Returns:
        str: HTML-formatted SQL code.
    """
    try:
        # Use the SqlLexer for T-SQL syntax highlighting
        lexer = SqlLexer()

        # Configure the HTML formatter
        formatter = HtmlFormatter(
            style=style,
            cssclass=cssclass,
            linenos=linenos,  # Add line numbers if requested
            noclasses=False,  # Use CSS classes for styling
        )

        # Highlight the SQL code
        formatted_code = highlight(sql_code, lexer, formatter)

        # Return the formatted HTML
        return formatted_code

    except Exception as e:
        print(f"Error formatting SQL code: {e}")
        return sql_code  # Return the original code if formatting fails
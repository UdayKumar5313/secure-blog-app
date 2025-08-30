# Secure Blog Application in Flask

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![License](https://img.shields.io/badge/License-MIT-green)

This project is a simple, database-driven blog application built with Python and the Flask web framework. It was developed as a portfolio piece to demonstrate secure coding practices and the remediation of a critical web vulnerability.

The application was intentionally built with an **SQL Injection (SQLi)** vulnerability for educational purposes. It was then patched to demonstrate the correct, secure way to handle database queries.

This application is the target for its companion project, the **[SQL Injection Vulnerability Scanner](https://github.com/UdayKumar5313/sql-injection-scanner)**.

## Project Purpose
The goal of this project is to showcase a full security lifecycle:
1.  **Building** a functional web application.
2.  **Identifying** a critical security flaw (SQLi).
3.  **Remediating** the flaw using industry-standard best practices.
4.  **Verifying** the fix.

## Security Vulnerability & Fix

* **Vulnerability:** The initial version of the application passed user input from a search form directly into an SQL query using an f-string. This allowed an attacker to inject malicious SQL syntax (like a single quote `'`), causing the database to error and proving the vulnerability.

* **Remediation:** The vulnerability was patched by implementing **Parameterized Queries (Prepared Statements)**. Instead of formatting the user input into the query string, the input is passed as a separate parameter to the database driver. The driver then safely handles the input, preventing any malicious characters from affecting the SQL command's structure.

    **Vulnerable Code:**
    ```python
    query = f"SELECT * FROM post WHERE title LIKE '%{query_param}%'"
    cursor.execute(query)
    ```
    **Secure Code:**
    ```python
    query = "SELECT * FROM post WHERE title LIKE ?"
    cursor.execute(query, (f'%{query_param}%',))
    ```

## How to Run
1.  Clone the repository and `cd` into it.
2.  Create and activate a virtual environment (`venv`).
3.  Install dependencies: `pip install -r requirements.txt`
    *(Note: You will need to create a `requirements.txt` file with the content `Flask` and `Flask-SQLAlchemy`.)*
4.  Initialize the database: `flask shell` then `db.create_all()` and `exit()`.
5.  Run the application: `flask run`. The app will be available at `http://127.0.0.1:5000`.

## License
This project is licensed under the MIT License.

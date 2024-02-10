# debstcyr datafun-05-SQL
# P5: Python and SQL Project

## Overview
'''Project 5 integrates Python and SQL, focusing on SQLite database interactions. This project introduces logging and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.'''

# Project Deliverables
-Author Data
-Book Data

# External Dependencies
-pandas
-pyarrow


# Initialize venv
py -m venv .venv

# Activate powershell script
.\.venv\Scripts\Activate.ps1

# Install Panda, numpy, seaborn
py -m pip install pandas 
py -m pip install numpy
py -m pip install seaborn
py -m pip install matplotlib

# Execute freeze dependencies
py -m pip freeze > requirements.txt

# Objective 
Create a Python script demonstrating the ability to interact with a SQL database, including creating a database, defining a schema, and executing various SQL commands. Incorporate logging to document the process and provide user feedback.

# Environment Setup
Create and activate a Python virtual environment for the project.
You can install all required packages into your local project virtual environment.
After you install the required dependencies, you can redirect the output of the pip freeze command to a requirements.txt file in your root project folder.
Document the process and commands you used in your README.md.
Add a .gitignore file to your project to exclude the virtual environment folder, your .vscode settings folder, and any other files that must not be committed to GitHub.
Terminal Commands: Windows example - record your process in your README:

py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install pandas pyarrow
py -m pip freeze > requirements.txt

# Start Project
In your Python file, you can create a docstring with a brief introduction to your project.

# Import Dependencies
import sqlite3
import pandas as pd
import pathlib.Path

## Logging
Logging is recommended for most professional projects. Implement logging to enhance debugging and maintain a record of program execution.

Configure logging to write to a file named log.txt.
Log the start of the program using logging.info().
Log the end of the program using logging.info().
Log exceptions using logging.exception().
Log other major events using logging.info().
Log the start and end of major functions using logging.debug().

import logging
# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

# Schema Design and Database Creation
Design a schema with at least two related tables, including foreign key constraints. Document the schema design in your README.md.

Implement a Python script to create the database, tables, and populate the tables. Keep each SQL statement in a separate file.
import sqlite3
import pandas as pd
import pathlib

# Your code here....

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()

# SQL Operations
Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements. You might create an additional table, insert new records, and perform data querying (with filters, sorting, and joining tables), data aggregation, and record update and deletion.

Include the following SQL files:

create_tables.sql - create your database schema using sql
insert_records.sql - insert at least 10 additional records into each table.
update_records.sql - update 1 or more records in a table.
delete_records.sql - delete 1 or more records from a table.
query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
query_filter.sql - use WHERE to filter data based on conditions.
query_sorting.sql - use ORDER BY to sort data.
query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

# Python and SQL Integration
Use Python to interact with the SQL database and execute SQL commands:
import sqlite3
def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

# Define Main Function 
Implement a main() function to execute the project SQL operations logic.

def main():
    db_filepath = 'your_database.db'

    # Create database schema and populate with data
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operations completed successfully")

# Conditional Script Execution
By using standard boilerplate code, ensure the main function only executes when the script is run directly, not when imported as a module.

## Module Design
Include a docstring at the top of the file describing its purpose.
The code should be clear, well-organized, and demonstrate good practices.
Include comments and docstrings for clarity.










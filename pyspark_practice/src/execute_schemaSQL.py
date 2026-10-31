import mysql
from config.mysql_config import get_mysql_config
from mysql.connector import Error
from pathlib import Path
from dotenv import load_dotenv
import os

# Đọc file .env tại thư mục gốc D:\de_rm
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

DATABASE_NAME = os.getenv("MYSQL_DATABASE")

schema_sql_path = Path(__file__).resolve().parent / "schema.sql"
def connect_to_mysql(config:dict):
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except Error as e:
        raise Exception(f'Cannot connect to mysql:{e}') from e

def create_db(cursor, db_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"Database {db_name} created")

def execute_sql_file(cursor, file_path : Path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    sql_commands = [cmd.strip() for cmd in sql_script.split(';') if cmd.strip()]

    for cmd in sql_commands:
        try:
            cursor.execute(cmd)
            print(f'executed: {cmd.strip()[:50]}')
        except Error as e:
            print(f'Error executing SQL: {e}')
            raise
# with open(schema_sql_path, 'r') as file:
#     sql_script = file.read()
# sql_commands = sql_script.split(';')
# print(sql_script)
# print(sql_commands)
# for command in sql_commands:
#     if command.strip():
#         cursor.execute(command)
#         print(f'executed: {command.strip()[:50]}')

def main():
    connection = None
    cursor = None

    try:
        # Get database config
        db_config = get_mysql_config()

        # Loại bỏ trường database
        config = {k: v for k, v in db_config.items() if k != 'database'}

        # Connect to MySQL
        connection = connect_to_mysql(config)
        cursor = connection.cursor()

        # Create database
        create_db(cursor, DATABASE_NAME)

        # Select database
        cursor.execute(f"USE `{DATABASE_NAME}`")

        # Execute SQL file
        execute_sql_file(cursor, schema_sql_path)

        print("---------SUCCESSFULLY----------")

    except Error as e:
        print(f"MySQL Error: {e}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    main()
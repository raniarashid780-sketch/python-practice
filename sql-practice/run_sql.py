import sqlite3
import traceback
from pathlib import Path

# Use paths relative to this script so it works regardless of CWD
BASE = Path(__file__).resolve().parent
DB_PATH = BASE / 'practice.db'
SQL_PATH = BASE / 'day01.sql'

conn = sqlite3.connect(str(DB_PATH))

with open(SQL_PATH, 'r', encoding='utf-8') as f:
    sql = f.read()

for statement in sql.strip().split(';'):
    statement = statement.strip()
    if statement:
        try:
            cursor = conn.execute(statement)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
        except Exception as e:
            print(f"Error executing statement: {statement!r}")
            traceback.print_exc()

conn.close()
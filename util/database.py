import sqlite3
import yaml
config = yaml.safe_load(open('config/sinoPec.yaml'))

def db_init():
    # Connect to a database file (or create it if it doesn't exist)
    conn = sqlite3.connect(config['db_name'])
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Create a table named 'users'
    with open('sql/init_sinopec.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)
    # Commit the changes to the database
    conn.commit()
    return


def db_insert(users_to_add):
    conn = sqlite3.connect(config['db_name'])
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO winners (id, winner, contact, date) VALUES (?, ?, ?, ?)", users_to_add)
    conn.commit()
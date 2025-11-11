import sqlite3
from datetime import datetime

DB_PATH = "database/parking.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_plate TEXT,
        entry_time TEXT,
        exit_time TEXT,
        duration REAL,
        fee REAL
    )''')
    conn.commit()
    conn.close()

def add_vehicle(plate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO vehicles (license_plate, entry_time) VALUES (?, ?)", (plate, entry_time))
    conn.commit()
    conn.close()

def exit_vehicle(plate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # normalize input (remove spaces/newlines, make uppercase)
    plate = plate.strip().upper()

    cursor.execute("SELECT entry_time FROM vehicles WHERE UPPER(TRIM(license_plate))=? AND exit_time IS NULL", (plate,))
    row = cursor.fetchone()

    if row:
        from datetime import datetime
        entry_time = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        exit_time = datetime.now()
        duration = round((exit_time - entry_time).total_seconds() / 3600, 2)
        fee = round(duration * 2.5, 2)

        cursor.execute("""
            UPDATE vehicles
            SET exit_time=?, duration=?, fee=?
            WHERE UPPER(TRIM(license_plate))=? AND exit_time IS NULL
        """, (exit_time.strftime("%Y-%m-%d %H:%M:%S"), duration, fee, plate))

        conn.commit()
        print(f"[INFO] Vehicle {plate} exited after {duration} hours, fee: ${fee}")
    else:
        print(f"[WARN] No active entry found for plate: {plate}")

    conn.close()

def get_all_vehicles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicles ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
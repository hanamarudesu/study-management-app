import sqlite3

connection = sqlite3.connect("database/studyhub.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS study_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        topic TEXT,
        content TEXT,
        duration_seconds INTEGER NOT NULL,
        material TEXT,
        start_position TEXT,
        end_position TEXT,
        understanding_level INTEGER,
        next_plan TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

connection.commit()
connection.close()

print("study_recordsテーブルを作成しました！")
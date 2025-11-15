import sqlite3

def init_db():
    conn = sqlite3.connect('questions.db')  # Ensure the database filename matches your app
    cur = conn.cursor()
    
    # Drop the table if it already exists (only do this if you don't have critical data)
    cur.execute('DROP TABLE IF EXISTS questions_answers')

    # Create the table without the description column
    cur.execute('''
    CREATE TABLE questions_answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    );
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")

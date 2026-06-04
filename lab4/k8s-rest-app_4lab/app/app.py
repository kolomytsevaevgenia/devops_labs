from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres'),
        database=os.environ.get('DB_NAME', 'myapp'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres')
    )
    return conn

def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
        conn.close()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO visits (visit_time) VALUES (NOW())')
    cur.execute('SELECT COUNT(*) FROM visits')
    visit_count = cur.fetchone()[0]
    conn.commit()
    conn.close()
    
    return f'''<!DOCTYPE html>
<html>
<head><title>Hello Jane</title></head>
<body>
    <h1>Hello, Jane!</h1>
    <p>Количество посещений: {visit_count}</p>
</body>
</html>'''

@app.route('/items', methods=['GET'])
def get_items_api():
    return jsonify({'status': 'ok'})

@app.route('/items', methods=['POST'])
def add_item():
    return jsonify({'status': 'ok'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

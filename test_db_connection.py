import psycopg2

try:
    conn = psycopg2.connect(
        dbname="dog_anxiety_db",
        user="postgres",
        password="postgres123",
        host="localhost",
        port="5433"
    )
    print("✅ Connected to PostgreSQL successfully!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
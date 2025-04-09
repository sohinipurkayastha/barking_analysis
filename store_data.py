import psycopg2
import datetime
import numpy as np
import librosa

# Database connection details
DB_NAME = "dog_anxiety_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5433"

# Load the recorded audio
INPUT_FILE = "barking_sound.wav"
y, sr = librosa.load(INPUT_FILE, sr=None)

# Extract duration & frequency
duration = librosa.get_duration(y=y, sr=sr)
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
frequency = float(np.mean(spectral_centroid)) if spectral_centroid.size > 0 else 0

# Convert audio to binary data
with open(INPUT_FILE, "rb") as file:
    sound_wave = file.read()

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # Insert data into the barking_data table
    insert_query = """
    INSERT INTO barking_data (timestamp, sound_wave, frequency, duration)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, (datetime.datetime.now(), psycopg2.Binary(sound_wave), frequency, duration))

    # Commit and close connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Barking data successfully stored in PostgreSQL!")

except Exception as e:
    print(f"Error storing data: {e}")
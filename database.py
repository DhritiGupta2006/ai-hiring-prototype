import psycopg2

conn = psycopg2.connect(
    dbname="cygnusa",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

print("Connected to database successfully!")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO candidates
(name, resume_score, technical_score, psychometric_score, final_score, decision, rationale)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (
    "Alice", 80, 85, 90, 85, "Selected", "Good overall candidate"
))

conn.commit()
print("Data inserted successfully!")

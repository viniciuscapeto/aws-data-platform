import psycopg2

conn = psycopg2.connect(
    host="cloud-db.cx8amcqu28v3.sa-east-1.rds.amazonaws.com",
    database="postgres",
    user="cloudadmin",
    password="Jabiroska2026",
    port=5432
)

cursor = conn.cursor()

cursor.execute("""
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
""")

for tabela in cursor.fetchall():
    print(tabela)

conn.close()
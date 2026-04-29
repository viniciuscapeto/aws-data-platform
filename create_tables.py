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
CREATE TABLE IF NOT EXISTS dados_coletados (
    id SERIAL PRIMARY KEY,
    valor INT,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()

print("🔥 Tabela criada com sucesso!")

cursor.close()
conn.close()
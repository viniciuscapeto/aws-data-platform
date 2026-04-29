import psycopg2

conn = psycopg2.connect(
    host="cloud-db.cx8amcqu28v3.sa-east-1.rds.amazonaws.com",
    database="postgres",
    user="cloudadmin",
    password="Jabiroska2026",
    port=5432
)

print("🔥 Conectado com sucesso!")

conn.close()
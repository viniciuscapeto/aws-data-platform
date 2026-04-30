from api.services.db_service import execute_query


query = """
CREATE TABLE IF NOT EXISTS arquivos (
    id SERIAL PRIMARY KEY,
    nome_original TEXT NOT NULL,
    s3_key TEXT NOT NULL,
    bucket TEXT NOT NULL,
    data_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

execute_query(query)

print("Tabela arquivos criada com sucesso.")
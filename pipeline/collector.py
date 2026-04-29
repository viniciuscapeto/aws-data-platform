import random
from api.services.db_service import execute_query


def inserir_dado():
    valor = random.randint(1, 100)

    execute_query(
        "INSERT INTO dados_coletados (valor) VALUES (%s);",
        (valor,)
    )

    print(f"Dado inserido com sucesso: {valor}")


if __name__ == "__main__":
    inserir_dado()
from fastapi import APIRouter
from api.services.db_service import execute_query

router = APIRouter()


@router.get("/dados")
def listar_dados():
    dados = execute_query(
        "SELECT id, valor, data FROM dados_coletados ORDER BY id DESC LIMIT 10;",
        fetch=True
    )

    return {
        "dados": [
            {
                "id": row[0],
                "valor": row[1],
                "data": row[2]
            }
            for row in dados
        ]
    }
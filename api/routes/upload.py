from fastapi import APIRouter, UploadFile, File
from api.services.storage_service import upload_file_to_s3
from api.services.db_service import execute_query

router = APIRouter()


@router.post("/upload")
def upload(file: UploadFile = File(...)):
    result = upload_file_to_s3(file)

    execute_query(
        """
        INSERT INTO arquivos (nome_original, s3_key, bucket)
        VALUES (%s, %s, %s);
        """,
        (
            result["file_name"],
            result["s3_key"],
            result["bucket"]
        )
    )

    return {
        "message": "Arquivo enviado com sucesso",
        "file_name": result["file_name"],
        "s3_key": result["s3_key"],
        "bucket": result["bucket"]
    }
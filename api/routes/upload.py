from fastapi import APIRouter, UploadFile
from api.services.storage_service import upload_file

router = APIRouter()

@router.post("/upload")
def upload(file: UploadFile):
    url = upload_file(file)
    return {"url": url}
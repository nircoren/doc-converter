from fastapi import APIRouter,  File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import os

from ..docs.index import convert_files_to_doc

router = APIRouter(
    prefix="/doc",
    tags=["doc"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@router.get("/")
def main():
    return 'waas'

@router.post("/convert")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        request_data = {
            "files" : contents,
            "action_name" : 'convertion_1',
        }
        doc_id = convert_files_to_doc(request_data)
        # Additional processing can be done here (e.g., save to a file, process contents)
        return JSONResponse(content={"filename": file.filename, "message": "File uploaded successfully"}, status_code=200)
    finally:
        await file.close()

@router.get("/download/{file_name}")
async def download_file(file_name: str):
    file_location = f"../upload/{file_name}"
    return FileResponse(path=file_location, filename=file_name, media_type='application/octet-stream')

"""
@router.post("/convert")
def upload_file():
    file = request.files.get('hahira')
    request_data = {
        "files" : request.files,
        "action_name" : request.form.get('action_name'),
    }
    doc_id = convert_files_to_doc(request_data)
    return jsonify({"data": doc_id + '.docx'})

@router.get("/download/{item_id}")
def download_file(filename):

    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    results_dir = os.path.join(base_dir, 'results')
    return send_from_directory(results_dir, 'res-' + filename, as_attachment=True)
"""
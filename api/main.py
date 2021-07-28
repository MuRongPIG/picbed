from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from os.path import dirname, abspath, join
import time 

app = FastAPI()
dir = dirname(abspath(__file__))
@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open(join(dir, '..', 'data',"{}.jpg").format(str(time.time()*1000000)[:-2],), "wb",) as f1:
        f1.write(contents)
    return {
        "success" : "True",
        "filename": file.filename
        }

@app.get("/get")
async def get_file(name :str):
    return FileResponse('{}.jpg'.format(name))
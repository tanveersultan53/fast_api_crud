from fastapi import FastAPI
from Api import notes
from database import engine,metadata,database

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await  database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"hello":"test_route"}

@app.get("/test")
def read_root1():
    pass

app.include_router(notes.router, prefix="/notes", tags=["notes"])


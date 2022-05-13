from fastapi import APIRouter
from fastapi.params import Path
from Api.models import NoteSchema,NoteDB
from fastapi.exceptions import HTTPException
from Api import cruds
from typing import List

router = APIRouter()

@router.get("/{id}/",response_model=NoteDB)
async def read_note(id:int=Path(...,title="the note id is required")):
    note = await cruds.get(id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/",response_model=List[NoteDB])
async def read_all_notes():
    return await cruds.get_all()



@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await cruds.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object

@router.delete("/{id}/",response_model=NoteDB)
async def read_note(id:int=Path(...,title="the note id is required")):

    note = await cruds.delete(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put('/{id}/',response_model=NoteDB)
async def update_note(payload:NoteSchema,id:int=Path(...,title="Note id Required!")):
    note = await cruds.get(id=id)
    if not note:
        raise HTTPException(status_code=404,detail="Note not Exist")
    note_id = await cruds.put(id,payload=payload)
    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object
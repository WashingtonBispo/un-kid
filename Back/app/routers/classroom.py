from fastapi import APIRouter, HTTPException
from ..services.classroom import post, getAll, get
from ..domain.classroom import ClassroomJSON

router = APIRouter(
    prefix="/classroom",
    tags=["Classroom"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", name='Get All Classrooms')
async def read_items():
    return getAll()

@router.get("/{id}", name='Get Classroom By Id')
async def getClassroom(id: str):
    return get(id)

@router.post("/", name='Post Classroom')
async def postClassroom(json: ClassroomJSON):
    response = post(json)
    return response
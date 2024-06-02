from fastapi import APIRouter, HTTPException
from ..services.account import post, getAll, get
from ..domain.account import AccountJSON

router = APIRouter(
    prefix="/account",
    tags=["Account"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def getAllAccount():
    return getAll()

@router.post("/", name='Post Account')
async def postAccount(json: AccountJSON):
    return post(json)

@router.get("/{id}", name='Get Account By Id')
async def getAccountById(id: str):
    return get(id)

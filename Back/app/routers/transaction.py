from fastapi import APIRouter, HTTPException
from ..services.transaction import post, getAll, get, delete
from ..domain.transaction import TransactionJSON

router = APIRouter(
    prefix="/transaction",
    tags=["Transaction"],
    responses={404: {"description": "Not found"}},
)

@router.get("/",name='Get All Transaction')
async def getAllTransaction():
    return getAll()

@router.get("/{id}",name='Get Transaction By Id')
async def getTransactionById(id: str):
    return get(id)

@router.post("/", name='Post Transaction')
async def postTransaction(json: TransactionJSON):
    response = post(json)
    return response

@router.delete("/{id}",name='Delete Transaction By Id')
async def deleteTransactionById(id: str):
    return delete(id)
from fastapi import FastAPI

from .routers import classroom, account, transaction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(swagger_ui_parameters={"deepLinking": False})

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(classroom.router, prefix="/api")
app.include_router(account.router, prefix="/api")
app.include_router(transaction.router, prefix="/api")


@app.get("/")
async def testAPI():
    return {"message": "Hi from API"}
from fastapi import FastAPI

from .routers import classroom, account, transaction


app = FastAPI(swagger_ui_parameters={"deepLinking": False})

app.include_router(classroom.router)
app.include_router(account.router)
app.include_router(transaction.router)


@app.get("/")
async def testAPI():
    return {"message": "Hi from API"}
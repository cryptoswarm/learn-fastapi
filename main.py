from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    """
    Hello world fn
    """
    return {"message": "helle world!"}


@app.get("/items/{item_id}")
async def items(item_id: int):
    """
    Get items by id
    """
    return {"id": item_id, "name": "kronos"}

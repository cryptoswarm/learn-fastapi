from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    """
    Hello world fn
    """
    return {"message": "helle world!"}


# fixed path first
@app.get("/users/me")
async def get_current_user():
    """
    Get current user
    """
    return {"user": "you"}


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    """
    Get user by id
    """
    return {"user": user_id}


@app.get("/items/{item_id}")
async def items(item_id: int):
    """
    Get items by id
    """
    return {"id": item_id, "name": "kronos"}

from email import message

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from src.User.UserModel import UserModel as User
import json
from fastapi.responses import JSONResponse
from src.routes.api_router import mainRouter

with open('DummyUser.json') as f:
    DummyUser = json.load(f)
app = FastAPI(title="Application API",
    version="1.0.0")

app.include_router(mainRouter)  # Include the agents router
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "errors": [exc.detail]
        }
    )
@app.get("/")
async def read_root():
    return {"success": True, "message": "Hello, World with github!"}

@app.get("/users")
async def getAllUsers(name: str = None):
  if name:
    search_name = name.strip().lower()

    users = [
        user
        for user in DummyUser["users"]
        if search_name in f'{user["firstName"]} {user["maidenName"]} {user["lastName"]}'.lower()
    ]
  else:
    users = DummyUser["users"]
  return {"success": True, "message": "Get all users", "users": users}

@app.get("/users/{user_id}")
async def getUserById(user_id: int):
  for user in DummyUser[ "users" ]:
    if user["id"] == user_id:
      return {"success": True, "message": "Get user by id", "user": user}
  raise HTTPException(status_code=404, detail={
    "code": "User not found",
    "message": f"User with id {user_id} not found",
    "field": "user_id"
  })

@app.post("/user/create")
async def createUser(user: User):
  DummyUser["users"].append(user.dict())
  return {"success": True, "message": "User created", "user": user}

# Dic or pydantic -> interview question: How to convert a dictionary to a Pydantic model instance?
# Answer: You can use the Pydantic model's constructor to convert a dictionary to an instance of the model. For example: user = User(**user_dict)
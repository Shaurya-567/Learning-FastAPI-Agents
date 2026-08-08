from fastapi import FastAPI
from pydantic import BaseModel
import json

class User(BaseModel):
    id: int
    firstName: str
    maidenName: str
    lastName: str

with open('DummyUser.json') as f:
    DummyUser = json.load(f)
app = FastAPI()

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
  return {"success": False, "message": "User not found"}

@app.post("/user/create")
async def createUser(user: User):
  DummyUser["users"].append(user.dict())
  return {"success": True, "message": "User created", "user": user}

# Dic or pydantic -> interview question: How to convert a dictionary to a Pydantic model instance?
# Answer: You can use the Pydantic model's constructor to convert a dictionary to an instance of the model. For example: user = User(**user_dict)
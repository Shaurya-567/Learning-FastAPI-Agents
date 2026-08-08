from fastapi import APIRouter, HTTPException
from src.User import controller as user_controller
users_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@users_router.post("/create")
async def create_user():
    return user_controller.create_user()


@users_router.get("/getAllUser")
async def get_all_users(
    filter: str | None = None,
    sort: str | None = None,
    page: int = 1
):
    return {
        "success": True,
        "message": "Get all users",
        "filter": filter,
        "sort": sort,
        "page": page
    }


@users_router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    return {
        "success": True,
        "message": f"User {user_id} deleted"
    }
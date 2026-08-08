from fastapi import APIRouter
from src.agents.controller import controller as agent_controller


agents_router = APIRouter(
    prefix="/agent",
    tags=["Agents"]
)


@agents_router.post("/new-chat")
async def new_chat():
    return agent_controller.create_newChat()


@agents_router.delete("/delete-chat/{chat_id}")
async def delete_chat(chat_id: int):
    return agent_controller.delete_chat(chat_id)
from fastapi import APIRouter
from src.routes.agents_router import agents_router
from src.routes.use_route import users_router
mainRouter = APIRouter(prefix="/applications/v1", tags=["Main"])

mainRouter.include_router(agents_router)  
mainRouter.include_router(users_router) 
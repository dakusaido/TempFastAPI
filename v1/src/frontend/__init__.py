from fastapi import APIRouter

from v1.src.frontend import routers

router = APIRouter(
    prefix="/frontend"
)

router.include_router(routers.router)

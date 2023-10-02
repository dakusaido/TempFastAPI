from fastapi import APIRouter

from v1.src import frontend

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(frontend.router)

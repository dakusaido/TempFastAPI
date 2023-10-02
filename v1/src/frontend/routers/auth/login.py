from fastapi import APIRouter

from v1.src.datatypes.requests.frontend.auth import Login

router = APIRouter(
    prefix="/login"
)


@router.post(
    path=""
)
async def login(
        login_request: Login
):
    return "ok"

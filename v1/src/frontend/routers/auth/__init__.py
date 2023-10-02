from fastapi import APIRouter

from v1.src.frontend.routers.auth import email_verify, login, password_update, password_recovery, register

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(email_verify.router)
router.include_router(login.router)
router.include_router(password_recovery.router)
router.include_router(password_update.router)
router.include_router(register.router)

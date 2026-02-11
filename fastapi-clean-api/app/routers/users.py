from fastapi import APIRouter, Depends
from app.deps import get_current_user, admin_only
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def read_me(user: User = Depends(get_current_user)):
    return user

@router.get("/admin")
def admin_panel(user: User = Depends(admin_only)):
    return {"msg": f"Welcome admin {user.email}"}

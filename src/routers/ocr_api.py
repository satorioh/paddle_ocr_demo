from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
async def get_model_time():
    return {"lastUpdateTime": "success"}

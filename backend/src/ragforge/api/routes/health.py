from fastapi import APIRouter

router = APIRouter()

@router.get("/health/live", tags=["health"])
async def liveness() -> dict[str, str]:
    """Confirm that the API process is alive"""
    return {
        "status": "ok",
        "service": "ragforge-api"
    }
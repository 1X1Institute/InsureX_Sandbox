from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_claims():
    return [{"claim_id": 1, "status": "processed"}, {"claim_id": 2, "status": "pending"}]
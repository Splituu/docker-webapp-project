from fastapi import APIRouter

router = APIRouter()

@router.get("/results")
def get_results(race: str):
    return {
        "race": race,
        "season": 2025,
        "results": []
    }
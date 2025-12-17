from fastapi import FastAPI, Query, HTTPException
from app.services.openf1 import get_top10_results

app = FastAPI()

@app.get("/results")
def results(race: str = Query(..., description="Full name of the GP, e.g. 'Las Vegas GP'")):
    top10 = get_top10_results(race)
    if not top10:
        raise HTTPException(status_code=404, detail="Race not found or no results yet")
    return top10
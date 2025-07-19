from fastapi import FastAPI, HTTPException
from models.searchmodel import SearchRequest 
from utils.agent_utils import get_search_query

app = FastAPI()

@app.post("/search")
async def search(query: SearchRequest):
    try:
        search_results = await get_search_query(query.query)
        if search_results:
            return {"results": search_results}
        else:
            raise HTTPException(status_code=404, detail="No results found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
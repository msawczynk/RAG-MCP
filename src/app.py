from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import rag  # Import the RAG module

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post('/query')
def query_endpoint(request: QueryRequest):
    try:
        result = rag.perform_rag_query(request.query)
        return {'result': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000) 
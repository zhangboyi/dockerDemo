from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
@app.get("/test")
def get_items(item_id: int, name: str):
    return {
        "code": 200,
        "item_id": item_id,
        "name": name
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.main()
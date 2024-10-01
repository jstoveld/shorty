from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/shorty", response_class=HTMLResponse)
def get_form():
    return """
    <form method="post">
    <input type="text" name="url" placeholder="Enter your URL">
    <input type="submit">
    </form>
    """

@app.post("/shorty")
def submit_url(url: str = Form(...)):
    #TODO # We will take this URL and then shorten it here
    return {"submitted_url": url}
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

## Our Actual App will be here where we will shorten the URL
## We need to understand how the request will come in, store the original URL and then return the shortened URL
@app.post("/shorty")
def submit_url(url: str = Form(...)):
    #TODO # We will take this URL and then shorten it here

    #TODO # Return a 201 response with the shortened URL
    #TODO # Or we reply with a 400 response if the URL is not valid
    #TODO # Endpoint should return a 200 OK status code with the original URL
    #TODO # Update an existing short URL using a PUT method
    #TODO # Will need to validate the string to ensure there is nothing malicious happening.
    #TODO # Return a 204 response if the URL is successfully deleted
    #TODO # 200 OK code with the statustics of the URL (IE AccessCount: 10)
    return {"submitted_url": url}

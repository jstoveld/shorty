from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from urllib.parse import urlparse
import string
import random

import models
import db


app = FastAPI()


models.Base.metadata.create_all(bind=db.engine)


# Function / Dependancy to get the database session
# DONE # We need to create a database session
def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


# Function to validate our input URL
# DONE # Or we reply with a 400 response if the URL is not valid
# DONE # Will need to validate the string to ensure there is nothing malicious happening.
def validate_url(url: str) -> bool:
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])


# Default Route *Requirement 1*
# DONE # Redirect to /shorty
@app.get("/")
def read_root():
    return RedirectResponse(url="/shorty", status_code=301)


# Generate Shortened URL *Requirement 2*
# DONE Shortened URL works
def generate_short_url(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


## GET METHOD TO SEE ITEMS
## NOTE URL IS UNDER ITEMS /items/{short_url}
## DONE Get List of Items *Requierment 4*
@app.get("/shorty/items/{shortened_url}")
def read_item(shortened_url: str, db: Session = Depends(get_db)):
    item = db.query(models.URL).filter(models.URL.shortened_url == shortened_url).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


## DONE Form to collect the original LONG URL
## Shorty app GET function *Requierment 2*
@app.get("/shorty", response_class=HTMLResponse)
def get_form():
    return """
    <form method="post">
    <input type="text" name="url" placeholder="Enter your URL">
    <input type="submit">
    </form>
    """


## Our Actual App will be here where we will shorten the URL
#DONE # We will take this URL and then shorten it here
## Shorty app POST function *Requierment 3*
@app.post("/shorty")
def submit_url(url: str = Form(...), db: Session = Depends(get_db)):
    if not validate_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL")

    shortened_url = generate_short_url()
    db_url = models.URL(original_url=url, shortened_url=shortened_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return {"original_url": url, "shortened_url": shortened_url}

#DONE # Return a 201 response with the shortened URL
#DONE # Endpoint should return a 200 OK status code with the original URL
#DONE # 301 redirect original Long URL
## TODO Need to add a counter that updates the access_count
@app.get("/shorty/{shortened_url}")
def redirect_url(shortened_url: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.shortened_url == shortened_url).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    ## Increment the access count
    db_url.access_count += 1

    ## Commit the changes
    db.commit()
    db.refresh(db_url)

    return RedirectResponse(url=db_url.original_url, status_code=301)

#DONE # Return a 204 response if the URL is successfully deleted
@app.delete("/shorty/{shortened_url}", status_code=204)
def delete_url(shortened_url: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.shortened_url == shortened_url).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    db.delete(db_url)
    db.commit()
    return {"detail": "URL deleted successfully"}

    
#DONE # Update an existing short URL using a PUT method
## PUT method to update the long url or redirect target works now. To leverage via postman ensure that you are updating the request to Body - form-data, key new_url and the value is new long form URL or redirect target.
@app.put("/shorty/{shortened_url}")
def update_url(shortened_url: str, new_url: str = Form(...), db: Session = Depends(get_db)):
    if not validate_url(new_url):
        raise HTTPException(status_code=400, detail="Invalid URL")
    
    db_url = db.query(models.URL).filter(models.URL.shortened_url == shortened_url).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    db_url.original_url = new_url
    db.commit()
    db.refresh(db_url)

    return {"original_url": new_url, "shortened_url": db_url.shortened_url}



# DONE # 200 OK code with the statustics of the URL (IE AccessCount: 10)
## GET method to get the statistics of the short URL
@app.get("/shorty/{shortened_url}/stats")
def get_stats(shortened_url: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.shortened_url == shortened_url).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return {
        "original_url": db_url.original_url,
        "shortened_url": db_url.shortened_url,
        "access_count": db_url.access_count
    }

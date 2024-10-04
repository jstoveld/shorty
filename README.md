## Project URL
https://roadmap.sh/projects/url-shortening-service

# Shorty API

This is a RESTful API built with FastAPI and backed by a MySQL database. The API provides URL shortening services.

## Endpoints

### 1. Create a Short URL
- **Endpoint:** `/shorten`
- **Method:** `POST`
- **Description:** Creates a shortened URL.
- **Example URL:** `http://localhost:8000/shorten`
- **Request Body:**
    ```json
    {
        "long_url": "https://example.com"
    }
    ```

### 2. Retrieve a Short URL
- **Endpoint:** `/shorten/{short_id}`
- **Method:** `GET`
- **Description:** Retrieves the original URL from a shortened URL.
- **Example URL:** `http://localhost:8000/shorten/abc123`

### 3. Delete a Short URL
- **Endpoint:** `/shorten/{short_id}`
- **Method:** `DELETE`
- **Description:** Deletes a shortened URL.
- **Example URL:** `http://localhost:8000/shorten/abc123`

## Running the API

1. **Install dependencies:**
     ```bash
     pip install fastapi uvicorn mysql-connector-python
     ```

2. **Run the server:**
     ```bash
     uvicorn main:app --reload
     ```

## Database Configuration

Ensure your MySQL database is configured and accessible. Update the database connection settings in your FastAPI application accordingly.



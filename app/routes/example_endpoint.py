from fastapi import APIRouter

#ee for example endpoint
router = APIRouter(prefix="/ee")

@router.get("/example")
def example_endpoint():
    """An example FastAPI endpoint.

    Returns:
        dict: A dictionary containing a simple message.
    """
    return {"message": "Hello, this is an example endpoint!"}
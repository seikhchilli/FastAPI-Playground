from fastapi import APIRouter

#ude for user defined endpoint
router = APIRouter(prefix="/ude")

@router.get("/seikchilli")
def example_endpoint():
    """seikchilli FastAPI endpoint.

    Returns:
        dict: A dictionary containing a message.
    """
    return {
        "name": "Seikchilli",
        "userid" : "seikhchilli"
        }
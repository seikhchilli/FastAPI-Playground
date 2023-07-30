from fastapi import APIRouter

router = APIRouter(prefix="/userid")

@router.get("/hello")
def hello():
    """Hello user FastAPI endpoint.

    Returns:
        dict: A dictionary containing a message.
    """
    return {
        "name": "user_name",
        "userid" : "userid"
    }
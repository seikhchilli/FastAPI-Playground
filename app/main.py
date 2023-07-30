import os
from fastapi import FastAPI

app = FastAPI()

# Dynamically include all routes from the user_defined_endpoints package
router_directory = os.path.dirname(os.path.abspath(__file__)) + "/routes/user_defined_endpoints"
for filename in os.listdir(router_directory):
    if filename.endswith(".py") and filename != "__init__.py":
        route_module = filename[:-3]  # Remove the ".py" extension
        route_module_path = f"app.routes.user_defined_endpoints.{route_module}"
        router = getattr(__import__(route_module_path, fromlist=["router"]), "router")
        app.include_router(router)

# Include the example endpoint from example_endpoint.py
from app.routes import example_endpoint
app.include_router(example_endpoint.router)
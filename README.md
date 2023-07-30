# FastAPI-Playground

Welcome to the FastAPI-Playground repository! This is a place where you can experiment and play around with FastAPI by creating your own endpoints and trying out different features. Whether you are a first-time user or an experienced developer, this playground is designed to help you learn and explore the capabilities of FastAPI.

## Getting Started

To get started, follow the steps below:

1. Fork this repository to your GitHub account by clicking the "Fork" button in the top right corner of this page.

2. Clone your forked repository to your local machine:
```
git clone https://github.com/your-username/FastAPI-Playground.git
cd FastAPI-Playground
```
3. Install the required Python dependencies. It is recommended to set up a virtual environment before installing the dependencies:

```
python -m venv venv
source venv/bin/activate # On Windows, use "venv\Scripts\activate"
pip install -r requirements.txt
```

4. Run the FastAPI application:
```
uvicorn app.main:app --reload
```

The application will start, and you can access the FastAPI interactive API documentation at http://localhost:8000/docs.

## Example Endpoint

The repository comes with an example endpoint to demonstrate how to create an endpoint. You can find the example code in the `app/routes/example_endpoint.py` file. Feel free to explore the code and see how the endpoint is defined.

## Creating Your Own Endpoints

One of the primary purposes of this repository is to let you create your own endpoints and test them. You can do this by adding new Python files inside the `app/routes/user_defined_endpoints/` directory. Each file should define one or more endpoints using FastAPI decorators.

Here's a simple example of a user-defined endpoint:

```python
# app/routes/user_defined_endpoints/userid.py

from fastapi import APIRouter

router = APIRouter(/userid)

@router.get("/hello")
def hello_endpoint():
    return {
        "name": "user name",
        "userid" : "userid"
    }
```

- Save the file and commit it to your forked repository.
- Push the changes to your GitHub repository:

```
git add app/routes/user_defined_endpoints/my_custom_endpoint.py
git commit -m "Add my custom endpoint"
git push origin main
```

- Open a pull request (PR) from your forked repository to the original FastAPI-Playground repository. We will review your code and merge it if everything looks good.
- Once your PR is merged, your endpoint will be automatically included in the running FastAPI server, and you can test it using the interactive API documentation.

## Testing Your Endpoints

After your endpoint is added to the running server, you can test it by navigating to the appropriate URL in the interactive API documentation (Swagger UI) available at http://localhost:8000/docs. Use the provided interface to make requests to your endpoint and observe the responses.

## Contribution Guidelines

Contributions to this repository are welcome! The name of your route file should be `userid.py`. If you find a bug, have an enhancement in mind, or want to add more features, feel free to open an issue or submit a pull request. Please make sure to follow the coding standards and add appropriate tests for any new functionality.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

:yellow_heart: We hope you enjoy your time exploring FastAPI with this playground. Happy coding! :yellow_heart:
# Week 2: FastAPI
In this week's module, we'll be using Poetry dependency manager, and kickstart a minimal FastAPI application.

## Day 1 (W2-D1) : Poetry, and FastAPI: Hello World

<details>
<summary>Click to expand/collapse</summary>
  
### Poetry Dependency Manager (W2-D1-01)
1. Go to your workspace, and create a virtualenv if not already (Follow Week 1 Day 2)
2. Activate your virtualenv
```sh
# LINUX / Unix
source env/bin/activate

# Windows
./env/scripts/activate
```
3. Install Poetry
```sh
pip install poetry
```
4. Setup your poetry to define and customize your application


### Install FastAPI (W2-D1-02)
1. Use Poetry to install FastAPI and Uvicorn
```sh
poetry add FastAPI
poetry add uvicorn
```
2. Open VSCode with `main.py` and put the following code in it
```sh
code main.py
```

```py
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello World"
    
```
3. Save the file, and run the server
```sh
uvicorn main:app
```
4. Visit http://localhost:8000 or http://127.0.0.1:8000 to test your FastAPI application
</details>

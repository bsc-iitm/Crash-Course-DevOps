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

## Day 2 (W2-D2) : FastAPI request methods

<details>
<summary>Click to expand/collapse</summary>

### GET Method (W2-D2-01)
`The GET is a (HTTP) method that is applied while requesting information from a particular url`

GET request can't contain any `body` data in the request, any information is passed through the URL or through URL parameters. 

Example, `http://example.com/get/a/path?param1=value&param2=value2`

To make a GET request handler in FastAPI, 

```python

@app.get("/test/get")
async def test_get_request() -> str:
  return "GET request works!"
  
@app.get("/test/get_params")
async def test_get_params_request(name: str) -> str:
  return f"GET request with param, {name = }"
  
@app.get("/test/get_params2")
async def test_get_params_request2(
    name: str, 
    age: int, country: 
    str = "India (Default)"
  ) -> str:
  
  return f"GET request with param, {name = }, {age = }, {country = }"

```

Try to visit the following URIs to test the above methods,
- http://localhost:8000/test/get
- http://localhost:8000/test/get_params?name=Dote
- http://localhost:8000/test/get_params2?name=Dote&age=12
- http://localhost:8000/test/get_params2?name=Dote&age=12&country="Canada"

### POST Method (W2-D2-02)
`In the POST method, the data is sent to the server as a package in a separate communication with the processing script. Data sent through the POST method will not be visible in the URL`

POST request may contain data in the `body` section of the request, and can also contain URL params like in GET.

To make a POST request handler in FastAPI,

```python
@app.post("/test/post")
async def test_post() -> str:
  return "POST request works!"
```

To retrieve POST data in FastAPI you have to create a schema for the post data as Pydantic objects.

```python
from pydantic import BaseModel

class SampleData(BaseModel):
  name: str
  age: int
  country: str = "India (Default)"

@app.post("/test/post_data")
async def test_post_data(data: SampleData):
  return "POST request, data: {data.name = }, {data.age = }, {data.country = }"
  
```
  
To test POST requests, you can use tools like postman or install `requests` python module (`pip install requests`), and run the following
  
```python
immport requests
  
r = requests.post("http://localhost:8000/test/post")
print("POST response", r.text)

r = requests.post("http://localhost:8000/test/post_data", json={"name": "Dote", "age": 18,})
print("POST data 1 response", r.text)
  
r = requests.post("http://localhost:8000/test/post_data", json={"name": "Dote", "age": 18, country: "Canada"})
print("POST data 2 response", r.text)
```

### Other Method (W2-D2-03)

Like POST there are other similar methods, PATCH, DELETE, and PUT.

```python
from pydantic import BaseModel

class SampleData(BaseModel):
  name: str
  age: int
  country: str = "India (Default)"

@app.put("/test/put")
async def test_put_data(data: SampleData):
  return {
    "type": "PUT",
    "data": data,
  }

@app.patch("/test/patch")
async def test_patch_data(data: SampleData):
  return {
    "type": "PATCH",
    "data": data,
  }

@app.delete("/test/patch")
async def test_delete_data():
  return {
    "type": "DELETE",
    "data": None,
  }
```
</details>

## Day 3 (W2-D3) - Pydantic
<details>
<summary>Click to expand/collapse</summary>

Pydantic provides a model based data structure with data validation and settings management using Python's type hinting/annotations.

### Installation (W2-D3-01)

You can install this in your project by running the following poetry command,

```sh
poetry add pydantic
```

### Pydantic models - Base Model (W2-D3-02)

Import any model you want to define from pydantic's `BaseModel`, and you are done

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    salary: float

```

you can try creating objects for this model and verify if the data types are enforced

```python

print(User(id=1, name="Dote", age=21, salary=90000))
print(User(id="1", name="D.e", age=18, salary=8000.90))
print(User(id="1.0", name="Dote", age=21, salary=90000))
print(User(id=1, name=1234, age=21, salary=90000))
print(User(id=1, name="Dote", age=21.9, salary=90000))
print(User(id=1, name="Dote", age=21, salary="N/A"))
print(User(id=None, name="Dote", age=21, salary=90000))
print(User(id=1, name=None, age=21, salary=90000))

```

### Pydantic model conversions (W2-D3-03)

Most used feature of pydantic is it's ability to convert the model to dictionary or json.


```

user = User(id=1, name="Dote", age=21, salary=90000)

d = user.dict()
j = user.json()

print(d, type(d))
print(j, type(j))

```


### Pydantic extended annotation using typing
You can use Python 3's built in typing library to extend the type annotations

```python

from typing import List, Union, Tuple, Any, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    marks: Tuple[int]
    courses: List[str]
    remarks: Optional[Any]
    secret_key: Union[str, int]

```

try out the same,

```python

print(User(id=1, marks=(1, 2), courses=["cse"], secret_key="101a"))
print(User(id=1, marks=(1, 2), courses=["cse"], remarks="Good", secret_key=1009))

```

</details>

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/test/get")
async def test_get_request() -> str:
    return "GET request works !" 

@app.get("/test/get_params")
async def test_get_params_request(name: str) -> str:
    return f"GET request with params_request, {name =}"

@app.get("/test/get_params2")
async def test_params_request2(
    name: str,
    age: int,
    country: str="india (Default)"
    ) -> str:
    
    return f"GEt request with param,{name},{age},{country}"




class SampleData(BaseModel):
  name: str
  age: int
  country: str = "India (Default)"

@app.post("test/post")
async def post_request()-> str:
    return "post request works !"

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
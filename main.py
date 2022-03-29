#Python
import imp
from lib2to3.pgen2.token import OP
from typing import Optional

# Pydantic
from pydantic import BaseModel

# fastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()


# Models
class Person(BaseModel):
    firt_name : str
    last_name : str
    age : int
    hair_color : Optional[str] = None
    is_married : Optional[bool] = None

@app.get('/')
def home():
    return {"Hello":"World"}


@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person
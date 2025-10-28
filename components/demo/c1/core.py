from pydantic import BaseModel

class DemoC1(BaseModel):
    name: str
    age: int


def get_demo_c1():
    return "demo_c1"
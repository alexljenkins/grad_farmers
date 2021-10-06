# https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI
from fastapi.datastructures import DefaultPlaceholder
from .src.farmer.farm import Animal, Farm

app = FastAPI()

# should put this in a globals file
farm = Farm()

@app.get("/")
async def root():
    return "200"

@app.post("/add_animal")
async def add_animal_to_farm(animal:str, number_of_legs:int, number_of_animals:int):
    """ Remember that type annotations are required for FastAPI variables """
    farm.add_animal(Animal(animal, number_of_legs), number_of_animals)
    return farm

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port = 5555, host="0.0.0.0", reload=True)
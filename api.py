# https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI
from fastapi.datastructures import DefaultPlaceholder
from src.farmer.farm import Animal, Farm

app = FastAPI()

farm = Farm()

@app.get("/")
def root():
    return "200"

@app.post("/add_animal")
def add_animal_to_farm(animal:str, number_of_legs:int, number_of_animals:int):
    """ Remember that type annotations are required for FastAPI variables """
    farm.add_animal(Animal(animal, number_of_legs), number_of_animals)
    return farm
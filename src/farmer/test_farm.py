from .farm import Animal, Farm
import pytest

# basic method of unit testing:
def test_something_else():
    farm = Farm()
    farm.add_animal(Animal('dog', 4), 1)
    assert len(farm.animals) == 1
    assert farm.animals[0]['animal'].name == 'dog'
    assert farm.animals[0]['animal'].number_of_legs == 4

def test_add_animal_edge_cases():
    ...

def test_add_animal_failing():
    ...


# using pytest decorator for multiple tests at once
@pytest.mark.parametrize("name, legs, count",
                         [
                             ('cow', 4, 6),
                             ('dog', 4, 1),
                             ('dog', 4, -1),
                             ('dog', 0, 0),
                             
                         ])
def test_add_animal_working(name, legs, count):
    farm = Farm()
    farm.add_animal(Animal(name, legs), count)
    assert farm.animals[0]['animal'].name == name
    assert farm.animals[0]['animal'].number_of_legs == legs

# instead of if statements to separate out logic, better to use a separate test function
@pytest.mark.parametrize("name, legs, count, expected",
                         [
                             ('dog', -4, -1, 0),
                             ('dog', -4, 1, 0),

                             
                         ])
def test_add_animal_with_negative_legs(name, legs, count, expected):
    farm = Farm()
    farm.add_animal(Animal(name, legs), count)
    assert farm.animals[0]['animal'].name == name
    assert farm.animals[0]['animal'].number_of_legs == expected


# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function twice: once using positional arguments and once using keyword arguments.
def describe_pet(animal_type,pet_name):
    return animal_type ,pet_name
show=describe_pet
print(show("mamal","Elephant"))
print(show(pet_name="Dog",animal_type="Mamal"))
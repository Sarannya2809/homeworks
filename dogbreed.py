class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(f"{dog1.name} is a {dog1.breed} ({dog1.species})")
print(f"{dog2.name} is a {dog2.breed} ({dog2.species})")
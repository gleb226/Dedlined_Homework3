class Animal:
    def __init__(self, species):
        self.species = species
        self.hunger = 0
        self.tiredness = 0

    def sleep(self):
        print(f"The {self.species} is sleeping.")

    def increase_hunger(self, amount):
        self.hunger += amount
        print(f"The {self.species} feels hungry.")

    def increase_tiredness(self, amount):
        self.tiredness += amount
        print(f"The {self.species} feels tired.")


class Person:
    def __init__(self, name, age, animal_species):
        self.name = name
        self.age = age
        self.animal = Animal(animal_species)

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def provide_information(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

    def change_name(self, new_name):
        self.name = new_name
        print(f"Changed name to {self.name}.")

    def play_with_animal(self):
        print(f"{self.name} is playing with their {self.animal.species}.")

    def pet_animal(self):
        print(f"{self.name} is petting their {self.animal.species}.")

    def feed_animal(self):
        print(f"{self.name} is feeding their {self.animal.species}.")


person1 = Person("Alex", 12, "cat")
person2 = Person("Arina", 12, "dog")

person1.greet()
person2.greet()

person1.provide_information()
person2.provide_information()

person1.change_name("Peter")
person2.change_name("Emma")

person1.greet()
person2.greet()

person1.play_with_animal()
person2.pet_animal()

person1.feed_animal()
person2.feed_animal()

person1.animal.sleep()
person2.animal.increase_hunger(5)

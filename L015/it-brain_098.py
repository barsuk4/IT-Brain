class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Mammal(Animal):
    def __init__(self, name, species, diet_type):
        super().__init__(name, species)
        self.diet_type = diet_type

    def display_information(self):
        super().display_information()
        print(f"Diet Type: {self.diet_type}")


class Carnivore(Mammal):
    def __init__(self, name, species, diet_type, teeth_count):
        super().__init__(name, species, diet_type)
        self.teeth_count = teeth_count

    def display_information(self):
        super().display_information()
        print(f"Teeth Count: {self.teeth_count}")


class Lion(Carnivore):
    def __init__(self, name, species, diet_type, teeth_count, mane_size):
        super().__init__(name, species, diet_type, teeth_count)
        self.mane_size = mane_size

    def display_information(self):
        super().display_information()
        print(f"Mane Size: {self.mane_size}")


# Приклади для тестування
if __name__ == "__main__":
    lion = Lion("Lion", "Mammal", "Carnivore", 30, "Large")
    print("Information about Lion:")
    lion.display_information()
    print()

    carnivore = Carnivore("Carnivore", "Mammal", "Carnivore", 40)
    print("Information about Carnivore:")
    carnivore.display_information()
    print()

    mammal = Mammal("Mammal", "Mammal", "Herbivore")
    print("Information about Mammal:")
    mammal.display_information()



class animalCars:
    def __init__(self, make, model, year):
        self.make = make
        self.model =  model
        self.year =  year
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

viper =  animalCars("Dodge", "Viper", "1998-2012")
print(viper.model)
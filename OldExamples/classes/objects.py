class people:
    def __init__(self, name):
        self.name = name
        #self.sound = sound
    def __str__(self):
        return "I am " + self.name + " and I hate this class."

me = people("Kyle")
print(me)


'''
class Animal:

  def __init__(self, species, sound):
    self.species = species
    self.sound = sound
  def makeSound(self,times):
    for t in range(times): 
      print(self.sound)
  def __str__(self):
    return "I am a " + self.species + " and I make the sound " + self.sound
fido = Animal("Dog", "Woof")  #object reference
print(fido)
tigger = Animal("Tiger", "Rrroar")  #object reference
tigger.makeSound(15)

'''
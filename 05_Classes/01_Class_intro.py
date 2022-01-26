# OOP - Object Oriented Programming

class Dog:

    animal_kind = "canine"  # class variable

    def loud_bark(self):
        return self.bark().upper()

    def bark(self):  # method
        return "Woof! I am a " + self.animal_kind


fido = Dog()  # Instantiation - i.e. creating an INSTANCE of a class
lassie = Dog()
pluto = Dog()

print(fido, type(fido))
print(fido.animal_kind)
print(lassie.animal_kind)
fido.animal_kind = "feline"
print(fido.animal_kind)
print(lassie.animal_kind)

# class Cat:
#
#     family = "Felidae"
#
#     def scratch(self):
#         return "ooooooooo! I am a" + self.family




# Make fizzbuzz in the form of functions. Look at the areas where i can include functions.

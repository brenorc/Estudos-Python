# We use the "class" statement to create a class
class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = 0   # the leading underscore indicates the "age" property is
                        # intended to be used internally
                        # do not rely on this to be enforced: it's a hint to other devs

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

     # Another instance method
    def sing(self):
        return "Yo... Yo... Microphone check... One Two... One Two..."
    
    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species
    
# Calling our class
brian = Human("Brian")
brian.say("Hello")
print(brian.sing())

# Calling our class method
print("Brian is a {}".format(brian.get_species()))

# Inheritance allows new child classes to be defined that inherit methods and
# variables from their parent class.

# Using the Human class defined above as the base or parent class, we can
# define a child class, Superhero, which inherits variables like "species",
# "name", and "age", as well as methods, like "sing" and "grunt"
# from the Human class, but can also have its own unique properties.

class Superhero(Human):

    # Child classes can override their parents' attributes
    species = "Superhuman"

    # Children automatically inherit their parent class's constructor including
    # its arguments, but can also define additional arguments or definitions
    # and override its methods such as the class constructor.

    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):
        
        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpowers

        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        super().__init__(name)

        # add an additional instance method
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))

# Calling our child class
superman = Superhero("Clark Kent")
superman.say("Hello")
superman.boast()
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Function to print colored text
def print_colored_text(text, color):
    colors = {
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "reset": "\u001b[0m"
    }
    color_code = colors.get(color.lower())
    if color_code:
        print(f"{color_code}{text}{colors['reset']}")
    else:
        print(text)

# Data types

# Text type
print_colored_text("Text type", "blue")
help(str)

# Boolean type
print_colored_text("Boolean type", "blue")
help(bool)

# Numeric types
print_colored_text("Numeric types", "blue")
help(int)
help(float)
help(complex)

# Sequence types
print_colored_text("Sequence types", "blue")
help(list)
help(tuple)
help(range)

# Set type
print_colored_text("Set type", "blue")
help(set)
help(frozenset)

# Mapping type
print_colored_text("Mapping type", "blue")
help(dict)

# None type
print_colored_text("None type", "blue")
help(type(None))

# OOP concepts

# Classes
print_colored_text("Classes", "blue")
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

help(MyClass)

# Inheritance
print_colored_text("Inheritance", "blue")
class MyChildClass(MyClass):
    def __init__(self, value):
        super().__init__(value)

help(MyChildClass)

# Polymorphism
print_colored_text("Polymorphism", "blue")
def polymorphic_function(obj):
    obj.display()

help(polymorphic_function)

# Encapsulation
print_colored_text("Encapsulation", "blue")
class MyEncapsulationClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

help(MyEncapsulationClass)

# Random module
print_colored_text("Random module", "blue")
help(random)

# List comprehension
print_colored_text("List comprehension", "blue")
help(list.append)
help(list.extend)
help(list.insert)
help(list.remove)
help(list.pop)
help(list.index)
help(list.count)
help(list.sort)
help(list.reverse)

# Data structures
print_colored_text("Data structures", "blue")

# List
print_colored_text("List", "blue")
help(list)

# Tuple
print_colored_text("Tuple", "blue")
help(tuple)

# Set
print_colored_text("Set", "blue")
help(set)

# Dictionary
print_colored_text("Dictionary", "blue")
help(dict)

# Visualization

data_types = ["Text", "Boolean", "Numeric", "Sequence", "Set", "Mapping", "None"]
num_methods = [
    len(str.__dict__), len(bool.__dict__), len(int.__dict__), len(list.__dict__),
    len(set.__dict__), len(dict.__dict__), len(type(None).__dict__)
]

fig, ax = plt.subplots()

ax.bar(data_types, num_methods)
ax.set_xlabel("Data type")
ax.set_ylabel("Number of methods")
ax.set_title("Number of methods for each data type")

def animate(i):
    random.shuffle(num_methods)
    ax.clear()
    ax.bar(data_types, num_methods)
    ax.set_xlabel("Data type")
    ax.set_ylabel("Number of methods")
    ax.set_title("Number of methods for each data type (Animation)")

ani = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=True)

plt.show()

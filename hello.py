print("Hello world!")

def test():
    print("From function")

def username(txt):
    print(f"Hello {txt}")

def add(a=0, b=1):
    return f"Total sum: {a + b}"


class Testing:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def get_fullname(self):
        return f"{self.name} {self.lastname}"

    def get_capitalized_name(self):
        return f"{self.name.upper()}"

    def get_upper_lastname(self):
        return f"{self.lastname.upper()}"


print(add())
test()
username("test")

person = Testing("bob", "hund")

print(person.get_fullname())
print(person.get_capitalized_name())
print(person.get_upper_lastname())


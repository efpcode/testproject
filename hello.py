print("Hello world!")

def test():
    print("From function")

def username(txt):
    print(f"Hello {txt}")


class Testing:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def getFullname(self):
        return f"{self.name} {self.lastname}"


test()
username("test")

person = Testing("bob", "hund")

print(person.getFullname())


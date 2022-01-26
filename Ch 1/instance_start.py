# Create a basic class
class Book:
    # Python's special function to initialize the object, can be overwritten
    # This is not constructor, this is an intitalizer function
    def __init__(self, title, author, pages, price):
        # Add properties
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "Secret"

    # The underscore is like a private variable, this is just hinting the programmer
    # But Double Underscore prevents access outside class
    def setdiscount(self, amount):
        self._discount = amount

    # All objects require the self argument
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price*self._discount)
        return self.price


# Create Instances of the class
b1 = Book("Brave New World", "Pi", 314, 44.55)
b2 = Book("War & Peace", "PeeWee", 214, 22.55)

print(b1.getprice())
b1.setdiscount(0.5)
print(b1.getprice())

print(b1._discount)

# print(b1.__secret)  # will not work
print(b1._Book__secret)  # will work

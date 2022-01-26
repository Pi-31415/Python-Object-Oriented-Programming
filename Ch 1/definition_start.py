# Create a basic class
class Book:
    # Python's special function to initialize the object, can be overwritten
    # This is not constructor, this is an intitalizer function
    def __init__(self, title):
        self.title = title
    pass


# Create Instances of the class
b1 = Book("Brave New World")
b2 = Book("War & Peace")

print(b1.title)

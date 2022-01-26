# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


from multiprocessing.sharedctypes import Value


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK", "COMIC")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if(Book.__booklist == None):
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def getType(self):
        return self.booktype

    def __init__(self, title, booktype):
        self.title = title
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype


# TODO: access the class attribute

print("Book Types: ", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "COMIC")

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
print(thebooks)
thebooks.append(b1)
thebooks.append(b2)

for x in enumerate(thebooks):
    print(x[1].getType())

from relationship_app.models import *

newbook = Book(title="someday", author="benita")
new_librarian = Librarian(name="monica", library="ancient days")


# Query all books by a specific author.
def getbooks(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# List all books in a library.
def getbook(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Retrieve the librarian for a library.
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Create a class for the book model and include methods to add, update, and delete books
# to the NoSQL database
import uuid


class Book(object):
    def __init__(self, title, author, pages, status):
        self.id = uuid.uuid4().hex
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.pages}', '{self.status}')"

    def __str__(self):
        return f"Book: ID: {self.id} Title: '{self.title}', Author: '{self.author}', Pages: '{self.pages}', Status: '{self.status}')"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def add_book(self, db_hadle):
        # Add a book to the database, using the db_handle
        # to access the database. Check that the book doesn't
        # already exist in the database
        db_hadle.insert(self)

    def update_book(self, db_handle):
        # Update a book in the database, using the db_handle
        # to access the database. Check that the book exists
        # in the database
        db_handle.update(self)

    def delete_book(self, db_handle):
        # Delete a book from the database, using the db_handle
        # to access the database. Check that the book exists
        # in the database
        db_handle.remove(self)


# Create a member class for the database model and include methods to add, update, and delete members
# to the NoSQL database
class Member(object):
    def __init__(self, name, email, phone):
        self.id = uuid.uuid4().hex
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Member('{self.name}', '{self.email}', '{self.phone}')"

    def __str__(self):
        return f"Member: ID: {self.id} Name: '{self.name}', Email: '{self.email}', Phone: '{self.phone}')"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def add_member(self, db_handle):
        # Add a member to the database, using the db_handle
        # to access the database. Check that the member doesn't
        # already exist in the database
        db_handle.insert(self)

    def update_member(self, db_handle):
        # Update a member in the database, using the db_handle
        # to access the database. Check that the member exists
        # in the database
        db_handle.update(self)

    def delete_member(self, db_handle):
        # Delete a member from the database, using the db_handle
        # to access the database. Check that the member exists
        # in the database
        db_handle.remove(self)

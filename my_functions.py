from book import Book
import json
def print_options():
    print("Press a aspecific button for that action")
    print("1-create a new book")
    print("2-save books locally")
    print("3-load books from the disk")
    print("4-Issued book")
    print("5-return a book")
    print("6-update a book")
    print("7-show all books")
    print("8-show  a book")

def input_book_info():
    id = input('ID: ')
    name= input('NAME: ')
    description = input('DESCRIPTION: ')
    isbn = input('ISBN : ')
    page_count = int(input('PAGE_COUNT: '))
    issued = input('ISSUED: ')
    issued = (issued == 'y' or issued == 'Y')
    author = input('AUTHOR: ')
    year = int(input('YEAR: '))
    return {
        'id' :id,
        'name':name,
        'description':description,
        'isbn':isbn,
        'page_count':page_count,
        'issued':issued,
        'author':author,
        'year':year,

    }

def create_book():
    book_input = input_book_info()
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'],
                book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    print(book.to_dict())
    return book

def save_book(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file = open("books.dat","w")
        file.write(json.dumps(json_books, indent = 4))
    except:
        print("we had an error saving books")

def load_books():
    try:
        file = open("books.dat","r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj = Book(book['id'], book['name'], book['description'], book['isbn'],
                book['page_count'], book['issued'], book['author'], book['year'])
            books.append(new_obj)
        print("successful loaded books")
        return books
    
    except:
        print("File doesn't exist")

    #Find book function
    #take books and id
    #If fond returns the index of book in the book array

def find_book(books,id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
    return None

def issue_book(books):
    id = input("Enter the id of the book you want to issue: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book successfully issued")
    else:
        print("Could not find the book you want")

def return_book(books):
    id = input("Enter the id of the book you want to return: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book successfully returned")
    else:
        print("Could not find the book you want")

# update book function
# in the function parameter it takes books
# first it asks for the id input
# finds the book id
# if the book found... creates a new book using already writte functions
# the book is replaced with this book
# if book not found, we just say its not found

def update_book(books):
    id = input("Enter User's ID: ")
    index = find_book(books,id)
    if index != None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book successfully updated")
    else:
        print("We could not find your book")

# show  all books
def show_all_books(books):
    for book in books:
        print(book.to_dict())

# show book
def show_book(books):
    id = input("Enter your ID: ")
    index = find_book(books,id)
    if index != None:
        print(books[index].to_dict())
    else:
        print("we could not find the id")

    




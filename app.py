import my_functions
import os
my_functions.print_options()
option = input()
books = []
while option != 'x' and option != 'X':
    if option == '1':
        books.append(my_functions.create_book())
        
    elif option == '2':
        my_functions.save_book(books)
    elif option == '3':
        books = my_functions.load_books()
    elif option == '4':
        my_functions.issue_book(books)
    elif option == '5':
        my_functions.return_book(books)
    elif option == '6':
        my_functions.update_book(books)
    elif option == '7':
        my_functions.show_all_books(books)
    elif option == '8':
        my_functions.show_book(books)
    else:
        print("the given command doesn't exist...")
    input("press enter to continue..")
    os.system("cls")
    my_functions.print_options()
    option = input()
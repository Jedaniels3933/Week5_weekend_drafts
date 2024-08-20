
from mysql.connector import Error
from db_connect import connect_db, Error
from add_book import add_book
from borrow_book import borrow_book
from return_book import return_book
from search_book import search_book
from fetch_all_books import fetch_all_books
import os   
from add_user import add_user
from fetch_user import fetch_user
from add_author import add_author
from fetch_author import fetch_author
from fetch_all_authors import fetch_all_authors
from fetch_all_users import fetch_all_users
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    
    while True:
        action = input('''
    Welcome to the Library Management System, please choose an option:
1 - Customer Actions
2 - Book Actions
3 - Exit    
''')
        while True:
            if action == '1':
                user_menu()
            elif action == '2':
                book_menu()
            elif action == '3':
                break
            else:
                print("Invalid input. Please try again")
                break

def book_menu():
    
    while True:
        action = input('''
1 - Add Book
2 - Borrow a Book
3 - Return a Book
4 - Search for a Book
5 - Display all Books
6 - Back to Main Menu
7 - Clear Terminal
''')
        
        if action == '1':
            add_book()
        elif action == '2':
            borrow_book() 
        elif action == '3':
            return_book() 
        elif action == '4':
            search_book()
        elif action == '5':
            fetch_all_books()
        elif action == '6':
            main_menu()
        elif action == '7':
            clear()


def user_menu():
    while True:
        action = input('''
1 - Add a new user
2 - View user details
3 - Display all users
4 - Main Menu 
5 - Clear Terminal
''')
            
        if action == '1':
            add_user()
        elif action == '2':
            fetch_user() 
        elif action == '3':
            fetch_all_users() 
        elif action == '4':
            main_menu()
        elif action == '5':
            clear()


def author_menu():
    while True:
        action = input('''

1 - Add a new author
2 - View author details
3 - Display all authors
4 - Main Menu
5 - Clear Terminal  
''')
        
        if action == '1':
            add_author()
        elif action == '2':
            fetch_author()
        elif action == '3':
            fetch_all_authors()
        elif action == '4':
            main_menu()
        elif action == '5':
            clear()    




if __name__ == "__main__":      

    main_menu() 

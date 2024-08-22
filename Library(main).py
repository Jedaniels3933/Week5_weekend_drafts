from mysql.connector import Error
from db_connect import connect_db, Error
from add_book import add_book
from borrow_book import lend_a_book
from return_book import give_book_back
from search_book import search_for_book
from fetch_all_books import all_the_books
import os   
from add_user import add_user
from fetch_user import search_for_user
from add_author import add_author
from fetch_author import show_author
from fetch_all_authors import show_all_authors
from fetch_all_users import fetch_all_users

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    
    while True:
        action = input('''
    Welcome to the Library Management System, please choose an option:
1 - User Actions
2 - Book Actions
3 - Author Actions
4 - Exit   
''')
        while True:
            if action == '1':
                user_menu()
            elif action == '2':
                book_menu()
            elif action == '3':
                author_menu()
            elif action == '4':
                exit()
            else:
                print("Invalid input. Please try again")
                
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
            lend_a_book() 
        elif action == '3':
            give_book_back() 
        elif action == '4':
            search_for_book()
        elif action == '5':
            all_the_books()
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
            search_for_user() 
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
            show_author()
        elif action == '3':
            show_all_authors()
        elif action == '4':
            main_menu()
        elif action == '5':
            clear()    



main_menu()
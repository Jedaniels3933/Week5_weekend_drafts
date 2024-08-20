from db_connect import connect_db, Error

def add_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("Enter the title of the book: ").title()
            author = input("Enter the author of the book: ").title()
            genre = input("Enter the genre of the book: ").title()
            isbn = input("Enter the ISBN of the book: ")
            copies = input("Enter the number of copies: ")

            new_book = (title, author, genre, isbn, copies)

            query = "INSERT INTO books (title, author, genre, isbn, copies) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit() 
            print(f"New book {title} added successfully!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


if __name__ == "__main__":
    add_book()  
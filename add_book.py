from db_connect import connect_db, Error

def add_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("Enter the title of the book: ").title()
            isbn = input("Enter the ISBN of the book, no dashes necessary: ")
            
            author_id = int(input("Please enter the author id (numbers only): "))
            
            new_book = (title, isbn, author_id)

            query = "INSERT INTO books (title, isbn, author_id) VALUES (%s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit() 
            print(f"New book {title} has been added to the library- Thanks for the donation !")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
                print("Connection closed.")


if __name__ == "__main__":
    add_book()  
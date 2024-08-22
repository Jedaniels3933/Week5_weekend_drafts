from db_connect import connect_db, Error

def search_for_book():
        
    conn = connect_db()
    if conn is not None:
        try:
            book_id = input("Please enter the book id: ")
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE id = %s"

            cursor.execute(query, (book_id,))

            id, title, author_id, isbn, availability = cursor.fetchone()
            print(f"{id}: {title}, {author_id}, {isbn}, {availability}")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    search_for_book()   
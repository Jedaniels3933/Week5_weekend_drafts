from db_connect import connect_db, Error

def search_book():
        
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                title = input("Enter the title of the book: ").title()
                query = "SELECT * FROM books WHERE title = %s"
                cursor.execute(query, (title,))
                for id, title, author, genre, isbn, copies in cursor.fetchall():
                    print(f"{id}: {title}, {author}, {genre}, {isbn}, {copies}")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

if __name__ == "__main__":
    search_book()   
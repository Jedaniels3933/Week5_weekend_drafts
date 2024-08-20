from db_connect import connect_db, Error

def fetch_all_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM books;'
            cursor.execute(query)
            for id, title, author, genre, isbn, copies in cursor.fetchall():
                print(f"{id}: {title}, {author}, {genre}, {isbn}, {copies}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_all_books()           

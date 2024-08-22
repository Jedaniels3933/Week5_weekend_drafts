from db_connect import connect_db, Error

def all_the_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM books;'
            cursor.execute(query)
            for id, title, author_id, isbn, availability in cursor.fetchall():
                print(f"{id}: {title}, {author_id},  {isbn}, {availability}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    all_the_books()           

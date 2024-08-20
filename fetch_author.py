from db_connect import connect_db, Error
def fetch_author():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            author_name = input("Enter the name of the author: ").title()
            query = "SELECT * FROM authors WHERE author_name = %s"
            cursor.execute(query, (author_name,))
            for id, author_name in cursor.fetchall():
                print(f"{id}: {author_name}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_author()      

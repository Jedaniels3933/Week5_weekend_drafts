from db_connect import connect_db, Error
def show_all_authors():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM authors"
            cursor.execute(query)
            for id, author_name in cursor.fetchall():
                print(f"{id}: {author_name}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    show_all_authors() 
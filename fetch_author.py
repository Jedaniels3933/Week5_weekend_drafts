from db_connect import connect_db, Error
def show_author():
    conn = connect_db()
    if conn is not None:
        try:
            author_id = input("Please enter the author id: ")
            cursor = conn.cursor()
            
            query = "SELECT * FROM authors WHERE id = %s"
            cursor.execute(query, (author_id,))
            id, name, bio = cursor.fetchone()
            print(f"{id}: {name}, {bio}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    show_author()      

from db_connect import connect_db

def add_author():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            author_name = input("Enter the name of the author: ").title()
            query = "INSERT INTO authors (author_name) VALUES (%s)"
            cursor.execute(query, (author_name,))
            conn.commit() 
            print(f"New author {author_name} added successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    add_author()    
from db_connect import connect_db, Error

def add_author():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            name = input("Enter the name of the author: ").title()
            biography = input("Enter the author's biography: ")
            
            new_author = (name, biography)
            
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            
            cursor.execute(query, (new_author))
            conn.commit() 
            print(f"New author {name} added successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    add_author()    
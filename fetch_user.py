from db_connect import connect_db, Error

def search_for_user():
    conn = connect_db()
    if conn is not None:
        try:
            user_id = input("Please enter the user id: ")
            cursor = conn.cursor()

            query = "SELECT * FROM users_new WHERE id = %s;"

            cursor.execute(query, (user_id,))

            id, name, library_id = cursor.fetchone()
            print(f"{id}: {name}, {library_id}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() 
            print("Connection successfully close")

if __name__ == "__main__":
    search_for_user()


from db_connect import connect_db, Error

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = input("Enter the name of the user: ").title() 
            library_id = input("Enter a unique library ID: ")
            new_users = (name, library_id)
            query = "INSERT INTO users (name , library_id) VALUES (%s, %s)"
            cursor.execute(query, (new_users))
            conn.commit() 
            print(f"New user:  {name}  Library ID # {library_id} added successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


if __name__ == "__main__":
    add_user()
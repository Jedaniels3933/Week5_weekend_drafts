from db_connect import connect_db, Error

def add_user(): 
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            user_name = input("Enter the name of the user: ").title()
            user_email = input("Enter the email of the user: ")
            user_phone = input("Enter the phone number of the user: ")
            query = "INSERT INTO users (user_name, user_email, user_phone) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_name, user_email, user_phone))
            conn.commit() 
            print(f"New user {user_name} added successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


if __name__ == "__main__":
    add_user()
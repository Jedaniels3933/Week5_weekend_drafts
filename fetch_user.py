from db_connect import connect_db, Error

def fetch_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            user_name = input("Enter the name of the user: ").title()
            query = "SELECT * FROM users WHERE user_name = %s"
            cursor.execute(query, (user_name,))
            for id, user_name, user_email, user_phone in cursor.fetchall():
                print(f"{id}: {user_name}, {user_email}, {user_phone}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_user()


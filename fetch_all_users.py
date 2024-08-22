from db_connect import connect_db, Error
def fetch_all_users():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users_new;"
            cursor.execute(query)
            for id, name, library_id in cursor.fetchall():
                print(f"{id}: {name}, {library_id}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_all_users()   
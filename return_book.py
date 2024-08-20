from db_connect import connect_db, Error

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            customer_id = input("Enter the customer ID: ")
            book_id = input("Enter the book ID: ")
            return_book(customer_id, book_id)
            query = "DELETE FROM borrowed_books WHERE customer_id = %s AND book_id = %s"
            cursor.execute(query, (customer_id, book_id))
            conn.commit() 
            print(f"Book returned successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    return_book()   


from db_connect import connect_db, Error

def give_book_back():
    conn = connect_db()
    if conn is not None:
        try:
            book_id = input(f"Please enter the book id your will like to return: ")
            cursor = conn.cursor()

            query = "UPDATE books SET availability = True WHERE id = %s" 

            cursor.execute(query,(book_id,))
            conn.commit()

            select_query = "SELECT * FROM books WHERE id = %s "
            cursor.execute(select_query, (book_id,))
            # breakpoint()

            id, title, author_id, isbn, availability = cursor.fetchone()
            print(f"{id}: {title}, {author_id}, {isbn}, {availability}")
            print(f"{title} book, under {id} was returned successfully")

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
   give_book_back()   


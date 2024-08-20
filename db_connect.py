import mysql.connector
from mysql.connector import Error
def connect_db():
    db_name = 'ecom'   
    user = 'root'
    password = '!?12ABpp'
    host = 'localhost'  

    
    try: 
        conn= mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
            )

        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    
    except Error as e:
        print(f"Error{e}")
        return None
    

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
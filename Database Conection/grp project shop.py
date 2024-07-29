import mysql.connector


def create_database_structure():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="pythonDatabase",
        passwd="1234",
        database="shop"
    )
    dbcursor = db_connection.cursor()
    dbcursor.execute("CREATE DATABASE shop")
    dbcursor.execute(""" 
        CREATE TABLE books (
            id INT (10),
            name VARCHAR (20),
            pages INT (3), 
            amount FLOAT (20),
            quantity INT (10),
            PRIMARY KEY (id)
        )
    """)

    sql = "INSERT INTO books (id,name,pages,amount,quantity) VALUES (%s,%s,%s,%s,%s)"
    vals = [
        (1, "Atles CR", 80, 100, 10),
        (2, "Atles CR", 120, 160, 20),
        (3, "Atles Exersice", 80, 60, 20)
    ]
    dbcursor.executemany(sql, vals)
    db_connection.commit()


def database_connection():
    # Create database Connection
    global dbconnection
    global mycursor
    dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="shop"
    )
    mycursor = dbconnection.cursor()


def input_data_to_database():
    # Call the database
    database_connection()

    # Get Max id from database
    mycursor.execute("SELECT MAX(id) FROM books")
    max_id = mycursor.fetchone()
    if max_id[0] is None:
        max_id = 1
    else:
        max_id = max_id[0]
        max_id += 1

    print(f"\nYor New book id is {max_id}")
    name = input("Enter the books name and type : ")
    page = int(input("Enter the page amount : "))
    amount = float(input("Enter the amount of one book : Rs."))
    quantity = int(input("Enter the book quantity : "))

    sql = "INSERT INTO books (id,name,pages,amount,quantity) VALUES (%s,%s,%s,%s,%s)"
    vals = (max_id, name, page, amount, quantity)
    mycursor.execute(sql, vals)
    dbconnection.commit()
    print("\nData insert Successfull!")


def see_current_data_from_database():
    # Call the database
    database_connection()

    # Select data query
    mycursor.execute("SELECT * FROM books")
    records = mycursor.fetchall()
    books = []
    # Get data for a list
    for record in records:
        books_details = {
            "id": record[0],
            "name": record[1],
            "pages": record[2],
            "amount": record[3],
            "quantity": record[4]
        }
        books.append(books_details)

    print("\n----")
    print("List")
    print("----")
    for book in books:
        print(f"Book id : {book['id']} || Book name : {
              book["name"]} {book["pages"]}")

    enter_id = int(input("\nEnter id to contine : "))
    global found_id
    found_id = None

    for book in books:
        if book["id"] == enter_id:
            found_id = book
            break

    if found_id:
        print(f"\nId found successfully\nId is {found_id['id']}")
        print(f"{found_id["name"]} - {found_id["pages"]} pages")
        print(f"Amount is Rs:{found_id['amount']} \nQuantity is {
              found_id['quantity']}")
    else:
        print("\nEnter Invalid try again!")

    dbconnection.commit()


def update_data_from_database():
    # Ask the choice update or delete data
    choice = int(
        input("\n1.Update data \n2.Delete data\nEnter the number to contine : "))

    # Update the database
    if choice == 1:
        # Get data function
        see_current_data_from_database()
        print(f"\nUpdate id is {found_id['id']}")
        print(f"Name of book {found_id['name']} - {found_id['pages']} pages")
        print(f"Current quantity is {found_id['quantity']}")
        # Make new quanity
        new_quantity = input(
            "\nEnter the new added quantity(Leave space to keep current data) : ")
        if new_quantity:
            new_quantity = int(found_id['quantity']) + int(new_quantity)
        # Call the database
        database_connection()
        # Call sql
        sql = "UPDATE books SET quantity = %s WHERE id = %s"
        val = (new_quantity, found_id['id'])
        mycursor.execute(sql, val)

    elif choice == 2:
        # Get data function
        see_current_data_from_database()
        print(f"\nUpdate id is {found_id['id']}")
        print(f"Name of book {found_id['name']} - {found_id['pages']} pages")
        print(f"Quantity is {found_id['quantity']}")
        print(f"Amount is {found_id['amount']}")
        # call Sql
        mycursor.execute(f"DELETE FROM books WHERE id = {found_id['id']}")
    else:
        print("\nInput number is invalid!")

    dbconnection.commit()


def print_the_bill():
    # Call the database
    database_connection()

    # Get the found id
    see_current_data_from_database()

    selected_quantity = int(input("\nEnter quantity to buy : "))
    total_amount = found_id['amount'] * selected_quantity
    new_quantity = int(found_id['quantity']) - int(selected_quantity)

    # Update the database
    sql = "UPDATE books SET quantity = %s WHERE id = %s"
    val = (new_quantity, found_id['id'])
    mycursor.execute(sql, val)

    # Make the bill
    print('\n-------------------------------------------------------------------')
    print("Gunarat Gunarathna Book Shop,\nWakwalla Road Galle,\n011-5463467")
    print('-------------------------------------------------------------------')
    print('Name\t\t\tPages\t\tAmount\t\tQuantity')
    print('-------------------------------------------------------------------')
    print(f"{found_id['name']}\t\t{
          found_id['pages']}\t\t{found_id['amount']}\t\t{selected_quantity}")
    print('-------------------------------------------------------------------')
    print(f"Total amount : {total_amount}")

    print(f"\nCurrent quantity is : {new_quantity}")

    dbconnection.commit()


# Code the Programe menu
print("\n--------------------")
print("Welcome!\nGunarathna Book Shop,\nWakwalla Road Galle,\n011-5463467")
print("--------------------")

while True:
    print("\n----")
    print("Menu")
    print("----")

    user_choice = int(input(
        "1.Add books for system\n2.See the current data\n3.Update books from syste\n4.Print the Bill\n5.Exit the System\nEnter the number to contineu : "))

    if user_choice == 1:
        input_data_to_database()
    elif user_choice == 2:
        see_current_data_from_database()
    elif user_choice == 3:
        update_data_from_database()
    elif user_choice == 4:
        print_the_bill()
    elif user_choice == 5:
        break
    else:
        print("\nEnter Number invalid Plz try again!")

print("\nThank you!")

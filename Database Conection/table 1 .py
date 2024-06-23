import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tables"
)

mycursor = db_connection.cursor()

# mycursor.execute("""
#     CREATE TABLE table_corder (
#         OrderId INT(11),
#         OrderDate CHAR(10),
#         OrderTotal DECIMAL(10, 0),
#         CustomerId INT(11),
#         PRIMARY KEY (OrderId)
#     )
# """)

sql = "INSERT INTO table_corder (OrderId, OrderDate, OrderTotal, CustomerId) VALUES (%s, %s, %s, %s)"
vals = [
    (1, "2009-03-16", 89, 1),
    (2, "2009-03-17", 220, 2),
    (3, "2009-03-17", 117, 3),
    (4, "2009-03-26", 220, 3),
    (5, "2009-04-01", 32, 1)
]

mycursor.executemany(sql, vals)
db_connection.commit()

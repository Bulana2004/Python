import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tables"
)

mycursor = db_connection.cursor()
mycursor.execute(""" 
    CREATE TABLE table_orderline (
        PartId INT(11),
        OrderId INT(11),
        UnitPrice DECIMAL(10,0),
        QtyOrdered INT(11),
        QtySent INT(11),
        PRIMARY KEY (PartId,OrderId)
    )
""")

sql = "INSERT INTO table_orderline (PartId,OrderId,UnitPrice,QtyOrdered,QtySent) VALUES (%s,%s,%s,%s,%s)"
vals = [
    (2, 1, 220, 1, 0),
    (4, 1, 220, 1, 0),
    (3, 2, 15, 2, 1),
    (3, 3, 55, 1, 1),
    (1, 4, 16, 3, 3),
    (3, 4, 16, 2, 2),
    (5, 4, 16, 2, 2),
    (1, 5, 21, 2, 2)
]
mycursor.executemany(sql, vals)

db_connection.commit()

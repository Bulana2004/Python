import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tables"
)
dbcursor = db_connection.cursor()

dbcursor.execute(""" 
    CREATE TABLE table_part (
    PartId INT(11),
    PartName CHAR(30),
    UnitPrice INT(11),
    QtyInstock INT(11),
    Category CHAR(25),
    PRIMARY KEY (PartId)
    )
""")

sql = "INSERT INTO table_part (PartId,PartName,UnitPrice,QtyInstock,Category) VALUES (%s,%s,%s,%s,%s)"
vals = [
    (1, "Kitchen table", 220, 0, "Kitchen"),
    (2, "Mixing bowl", 15, 8, "Kitchen"),
    (3, "Cutting board", 19, 25, "Kitchen"),
    (4, "Pillow", 16, 18, "Bedroom"),
    (5, "Fleece blanket", 21, 5, "Bedroom")
]
dbcursor.executemany(sql, vals)

db_connection.commit()

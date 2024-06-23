import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tables"
)

mycursor = mydb.cursor()
# mycursor.execute("""
#     CREATE TABLE table_custormer (
#         CustormerId INT(11),
#         FamilyName CHAR(30),
#         GivenName CHAR(30),
#         Street CHAR(30),
#         City CHAR(30),
#         State CHAR(30),
#         PostCode INT(11),
#         DateOfBirth CHAR(10)
#     )
# """)

sql = "INSERT INTO table_custormer (CustormerId,FamilyName,GivenName,Street,City,State,PostCode,DateOfBirth) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
    (1, "Smith", "Fred", "12 West Street", "Rockhampton", "Qld", 4701, "8/15/1978"),
    (2, "Li", "Bruce", "45 East Street", "Melbourne", "Vic", 3040, "8/11/1972"),
    (3, "Noble", "Donna", "25 North Street", "Sedney", "NSW", 2015, "7/22/1969"),
    (4, "Singh", "Donna", "25 South Avenue",
     "Rockhampton", "QLD", 4700, "11/30/1981")
]

mycursor.executemany(sql, val)
mydb.commit()

from woocommerce import API
import pyodbc

# Connection to WordPress
wcapi = API(
    url="http://localhost:8080/wordpress",
    consumer_key="ck_da1021dfafd2208628c730e256229652b79a4ee7",
    consumer_secret="cs_112d2abf80537e107826810139c2d1c69f5a602c",
    version="wc/v3"
)

# Connection to Database and query

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=192.168.5.140;'
                      'DATABASE=Lufra;'
                      'UID=user;'
                      'PWD=DukatLufr@')

cursor = conn.cursor()

database = cursor.execute("SELECT [DUKAT$Item Ledger Entry].[Item No_], DUKAT$Item.[Description 2], SUM([DUKAT$Item Ledger Entry].Quantity) AS 'SUM'"
               " FROM [DUKAT$Item Ledger Entry] "
               "INNER JOIN DUKAT$Item ON [DUKAT$Item Ledger Entry].[Item No_] = DUKAT$Item.No_ "
               "WHERE [DUKAT$Item Ledger Entry].[Location Code] = 'W-TR'"
               " AND [DUKAT$Item Ledger Entry].[Item No_] = 'I-000252'"
               "GROUP BY [DUKAT$Item Ledger Entry].[Item No_], DUKAT$Item.[Description 2]")

# Create a dictionary and fill it with items from DB

stock_from_db = {}

for each in database:
    stock_from_db[each[1]] = int(each[2])

# Sent every item on dictionary to the WP, with ID of product

for each in stock_from_db:
    data = {
        "stock_quantity": stock_from_db[each]
           }
    print(wcapi.put(f"products/{each}", data).json())

# Get products from WP
# product = wcapi.get("products").json()

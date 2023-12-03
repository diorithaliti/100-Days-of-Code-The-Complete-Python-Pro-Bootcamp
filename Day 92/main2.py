import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=192.168.5.140;'
                      'DATABASE=Lufra;'
                      'UID=user;'
                      'PWD=DukatLufr@')

cursor = conn.cursor()

database = cursor.execute("SELECT [DUKAT$Item Ledger Entry].[Item No_], DUKAT$Item.[Description 2], SUM([DUKAT$Item Ledger Entry].Quantity) AS 'SUM'"
               " FROM [DUKAT$Item Ledger Entry] "
               "INNER JOIN DUKAT$Item ON [DUKAT$Item Ledger Entry].[Item No_] = DUKAT$Item.No_ "
               "WHERE [DUKAT$Item Ledger Entry].[Location Code] = 'W-TR' AND [DUKAT$Item Ledger Entry].[Item No_] = 'I-000252'"
               "GROUP BY [DUKAT$Item Ledger Entry].[Item No_], DUKAT$Item.[Description 2]")

stock_from_db = {}

for each in database:
    stock_from_db[each[1]] = int(each[2])

print(stock_from_db)
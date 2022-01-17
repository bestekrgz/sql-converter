import sqlite3
import pandas

con = sqlite3.connect("example.db")
cur = con.cursor()

df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn ", con)
print(df)
df.to_csv('example.csv', index=None)
df.to_excel('example.xlsx', index=None)

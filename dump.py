from db import connection, sql

query = "select * from users"

result = sql.execute(query)
rows = result.fetchall()
    
for row in rows:
    print(row)    

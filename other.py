import psycopg2

conn = psycopg2.connect("dbname=hendrydb user=hendrytest password=hendrytest")
cur = conn.cursor()

cur.execute("insert into accounts values(0, 'bob123', 'bob123@gmail.com', 'abcde1234', '2022-11-9');")
conn.commit()

cur.execute("select * from accounts")

result = cur.fetchall()
print(result)






cur.close()
conn.close()

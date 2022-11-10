import psycopg2

conn = psycopg2.connect("dbname=testdb user=test password=test") # connect

cur = conn.cursor() # perform db operations


cur.execute("insert into myorder values(1, 'car', '2022-11-2');")

conn.commit()

cur.execute("select * from myorder where id='1';")
result = cur.fetchall()

for i in result:
    print(i[0])




cur.close()
conn.close()

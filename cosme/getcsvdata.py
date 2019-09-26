import psycopg2
import csv
#path = "127.0.0.1"
#port = "60350"
#dbname = "Cosme"
#user = "postgres"
#password = "password"

#conText = "host={} port={} dbname={} user={} password={}"
#conText = conText.format(path, port, dbname, user, password)

#print("start connection")

connection = psycopg2.connect(database="cosme", user="postgres", password="Ohtaki3106")
connection.get_backend_pid()
cur = connection.cursor()

print("show")
#print(conText)

with open('cosme.csv', newline='') as csvfile:
    read = csv.reader(csvfile)
    print("done reading cdv")
    for row in read:
        #sql = "INSERT INTO cosme_data VALUES('{}','{}')"
        #sql = sql.format(str(row[0]).replace("/", "-"), row[1])
        sql = "INSERT INTO cosme_data VALUES('{}','{}','{}','{}','{}','{}')"

        #row[4]が評価しないの場合、row[4] = 0にする処理を追加
        if row[4] == "評価しない":
            row[4] = 0
        sql = sql.format(str(row[0]).replace("/", "-"), row[1], row[2], row[3], row[4], row[5])
        
        print("----------start db access----------")

        cur.execute(sql)
        connection.commit()

        print("----------end db access----------")

cur.close()
connection.close()

print("succeed")

import sqlite3
connect=sqlite3.connect('c://sqlite//hcl.db')
cur=connect.cursor()
# sql="""insert into file_log values(?,?);"""
# data=(3,'c:/Hcl_folder/program4.txt')
# cur.execute(sql,data)
# connect.commit()
cur.execute('select * from file_log ')
rows=cur.fetchall()
for r in rows:
    print(r)
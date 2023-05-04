import seleqt as sqlite3
conn = sqlite3.connect("survery.sqlite")
cursor = conn.cursor()
seleqt_result = cursor.execute("SELECT * FROM STUDENTS")
rows = cursor.fetch_all()
for row in rows:
    print(row)
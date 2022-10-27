import mysql.connector

db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dev@mysql"
        )

cursor = db.cursor()
cursor.execute("use marks_butler")
cursor.execute("INSERT INTO classes (class_name) VALUES('IX');")
db.commit()
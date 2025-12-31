import argparse
import sqlite3

conn=sqlite3.connect("family.db")
cursor=conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS family (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		Name TEXT NOT NULL,
		Age TEXT NOT NULL,
		Relation TEXT NOT NULL
	)
""")
conn.commit()

def add_data(Name, Age, Relation):
	cursor.execute("""
		INSERT INTO family (Name, Age, Relation) VALUES (?,?,?)
	""",
	(Name, Age, Relation)
	)
	conn.commit()
	print("family members are added")

def view_data():
	cursor.execute("""
		SELECT * FROM family;
	""")
	members=cursor.fetchall()
	print("family members are listed for display")
	for i in members:
		print(f"Name: {i[1]}, Age:{i[2]}, Relation: {i[3]}")

def update_data(get_age, row_id):
	cursor.execute("""
		UPDATE family SET Age=? WHERE id=?
	""",
	(get_age, row_id)
	)
	conn.commit()

	if cursor.rowcount == 0:
		print("No rows found to update")
	else:
		print("Family member details updated")

def family():
	parser=argparse.ArgumentParser()
	parser.add_argument("name")
	parser.add_argument("age")
	parser.add_argument("relation")

	args=parser.parse_args()

	print("Name: ",args.name)
	print("Age: ",args.age)
	print("Age: ",args.relation)
	return args.name,args.age,args.relation

get_name, get_age, get_relation=family()
add_data(get_name, get_age, get_relation)
view_data()
update_data(get_age, 4)

input("Press Enter to exit...")


#import sqlite3
import sqlite3

#obtain a connection to test.db
connection = sqlite3.connect('test.db')

#get a cursor
cursor = connection.cursor()

#create a new table
cursor.execute('DROP TABLE IF EXISTS Pizza_Users');
cursor.execute('CREATE TABLE Pizza_Users(id INT, first_name TEXT, last_name TEXT, pizza_karma INT)')

#insert records into our table
cursor.execute("INSERT INTO Pizza_Users VALUES(1, 'John', 'Smith', 500)")
cursor.execute("INSERT INTO Pizza_Users VALUES(2, 'Mike', 'Jones', 75)")
cursor.execute("INSERT INTO Pizza_Users VALUES(3, 'James', 'Bond', 1200)")

#save changes
connection.commit()

#select all the data from our table
cursor.execute("SELECT * FROM Pizza_Users")

#get the list of results and print them to the console
rows = cursor.fetchall()
for row in rows:
	print row

#update a record
cursor.execute("UPDATE Pizza_Users set pizza_karma = 650 where id = 1")

connection.commit()

#delete a record
cursor.execute("DELETE FROM Pizza_Users where id = 2")

connection.commit()

#close the connection
connection.close()
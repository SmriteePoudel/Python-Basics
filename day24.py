#Update Command in database
import mysql.connector
db = mysql.connector.connect(       
    host='localhost',
    user='root',
    database='broadwayclass'
)

myterminal = db.cursor()
update_name="US Dollar"
update_command= f" UPDATE exchangerate SET name ={update_name} where id = 4"
myterminal.execute(update_command)
db.commit ()
db.execute()
print(db)


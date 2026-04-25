import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='broadwayclass'
)
myterminal = db.cursor()

insert_query = f'INSERT INTO exchangrate(date,iso3,name,unit,buy,sell) VALUES("2024-06-20","USD","US Dollar",1,82.50,83.00)'
myterminal.execute(insert_query)

#CRUD Operations working with MySQL
db.commit()
print(db)


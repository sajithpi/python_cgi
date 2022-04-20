#!C:\Python\Python39\python.exe

print("Content-type:text/html\n\n");

import cgi
import mysql.connector
from email import message

form = cgi.FieldStorage()

message = form.getvalue("message_py")
image = form.getvalue("image_data")
print("url:",form.getvalue("image_data"))


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""

)

mycursor = mydb.cursor()


sql = "INSERT INTO user (name,image) VALUES (%s,%s)"
args = (message,image)
mycursor.execute(sql,args)
mydb.commit()
print(mydb)



print(message+"from python")
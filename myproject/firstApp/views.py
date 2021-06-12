from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vikasverma",
  database="mydatabase"
)
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def formdata(request):
    name = request.POST['Name']
    phone = request.POST['Phone number']
    email = request.POST['Email']
    msg = request.POST['Message']
    mycursor = mydb.cursor()
    sql = "INSERT INTO myclient VALUES (%s, %s, %s, %s)"
    val = (name, phone, email, msg)
    mycursor.execute(sql, val)
    mydb.commit()
    return HttpResponse(f"<script>alert('{name} we have recieved your message.');</script>")

    
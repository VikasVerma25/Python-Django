from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

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
    return render(request, 'formdata.html', {
        'myname': name, 'myphone':phone, 'myemail':email, 'mymsg': msg})
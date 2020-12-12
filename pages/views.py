from django.shortcuts import render, redirect

from contacts.models import Contact


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        
        # check if some profession selected 
        if 'profession' in request.POST:
            profession = request.POST["profession"]
        else:
            profession = ''

        message = request.POST["message"]

        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            profession=profession,
            message=message,
        )

        contact.save()

        return redirect('contacts')

    return render(request, "contacts.html")

from django.shortcuts import render, redirect
from django.contrib import messages

from contacts.models import Contact
from contacts.validation import is_emtpy_fields, get_profession


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        phone = request.POST["phone"]

        if not is_emtpy_fields(name, email, message):
            # get profession if selected
            profession = get_profession(request)

            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                profession=profession,
                message=message,
            )

            contact.save()

            messages.success(
                    request, "Запит успішно відправленно"
                )

            return redirect('contacts')
        else:

            # tempotary save for fillind form
            request.session['name']  = name
            request.session['email']  = email
            request.session['phone']  = phone
            request.session['message']  = message

            messages.error(
                request, "Не вдалося відправити питання. Ви не заповнили обов'язкові поля."
            )
            
            return redirect('contacts')


    context = {}

    #if this is second try fill values
    if len(request.session.keys()) > 0:
        for key, value in list(request.session.items()):
            context[key] = value
            del request.session[key]

    return render(request, "contacts.html", context)

from django.shortcuts import render, redirect
from django.contrib import messages

from contacts.models import Contact
from contacts.validation import is_emtpy_fields, get_profession
from elements.calculation import calculate


def index(request):
    # context = {}

    # if 'load1' in request.session.keys():
    #     print('yes')
    #     context['load1'] = request.session['load1']
    # if 'load2' in request.session.keys():
    #     context['load2'] = request.session['load2']

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        question = request.POST["question"]
        phone = request.POST["phone"]

        if not is_emtpy_fields(name, email, question):
            # get profession if selected
            profession = get_profession(request)

            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                profession=profession,
                question=question,
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
            request.session['question']  = question

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

def results(request):
    if request.method == "POST":

        load1 = request.POST["load1"]
        load2 = request.POST["load2"]

        try:
            load1 = int(load1)
            load2 = int(load2)
        except:
            load1 = 0
            load2 = 0 

        load = load1 + load2

        lenght = 0
        step = 0
        
        if 'customgrid' in request.POST:
            try:
                lenght = request.POST['lenght']
                step = request.POST['step']
                if ',' in lenght:
                    lenght = lenght.replace(',', '.')
                if ',' in step:
                    step = step.replace(',', '.')
                lenght = float(lenght)
                step = float(step)
            except:
                pass

        else:
            grid = request.POST['grid'].split()
            print(grid)
            try:
                lenght = float(grid[0])
                step = float(grid[1])
            except:
                pass
        

        parametrs = calculate(lenght, step, load)

        
        
        # if 'grid' in request.POST:
        #     grid = request.POST["profession"]
        # else:
        #     lenght = request.POST["lenght"]
        #     step = request.POST['step']
        # return profession

        # question = request.POST["question"]
        # phone = request.POST["phone"]

        # request.session['custom_grid'] = True

        # request.session['load1']  = load1
        # request.session['load2']  = load2


        request.session['main_beam_height']  = parametrs['main_beam_height']
        request.session['secondary_beam_height']  = parametrs['secondary_beam_height']
        request.session['slab_height']  = 140
        request.session['profiled_sheet_height']  = 60
        request.session['main_height']  = parametrs['main_height']
        request.session['hole_height']  = parametrs['hole_height']
        request.session['hole_width']  = parametrs['hole_width']


        return redirect('results')

    context = {}

    for key, value in list(request.session.items()):
        context[key] = value

    return render(request, "results.html", context)

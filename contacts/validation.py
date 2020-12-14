def is_emtpy_fields(*args):
    for field in args:
        if not field.strip():
            return True
    return False

def get_profession(request):
    if 'profession' in request.POST:
        profession = request.POST["profession"]
    else:
        profession = ''
    return profession



        
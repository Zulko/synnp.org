from django.shortcuts import render

def index(request):
    """ Landing Page """
    return render(request, 'index.html')


def about(request):
    """ Project Info Page """
    return render(request, 'about.html')


def db_view(request):
    """ View of the database """
    return render(request, 'db_view.html')
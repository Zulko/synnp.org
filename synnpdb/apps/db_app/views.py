""" Views for the base application """


import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def pathways(request):
    return render(request, 'pathways.html')

""" Views for the base application """


import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
import models


@login_required
def pathways(request):
    return render(request, 'pathways.html')


@login_required
def autotable(request):
    print request.get("model")
    model = models.__dict__[request.get("model", "Oligo")]
    data = serializers.serialize("json", model.objects.all())
    print data
    return data

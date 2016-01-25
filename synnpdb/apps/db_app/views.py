""" Views for the base application """


import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from json2html import json2html
import models


@login_required
def parts(request):
    return render(request, 'table_parts.html')

@login_required
def compounds(request):
    return render(request, 'table_compounds.html')



@login_required
def autotable(request):
    request_model = request.GET["model"]
    model = models.__dict__[request_model]
    fields = request.GET["fields"].split(",")
    objects = model.objects.all()
    objects = [
        {
            field: e.__dict__[field]
            for field in fields
        }
        for e in objects
    ]

    for obj in objects:
    	obj["name"] = '<a href="/display_object/?model=%s&part_id=%s">%s</a>'%(
    		request_model, obj["id"], obj["name"]
    	)
    print json.dumps(objects, sort_keys=True, indent=4, separators=(',', ': '))
    return JsonResponse(objects, safe=False)


@login_required
def autoform(request):
    print request.get("model")
    model = models.__dict__[request.get("model", "Oligo")]
    data = serializers.serialize("json", model.objects.all())
    return JsonResponse(data)



def demo_spreadsheet(request):
    return render(request, 'demo_spreadsheet.html')


def display_object(request):
    object_id = request.GET["part_id"]
    model = models.__dict__[request.GET["model"]]
    obj = model.objects.get(id=object_id)
    data = serializers.serialize('json', [obj,])
    struct = json.loads(data)[0]["fields"]
    table = json2html.convert(json=struct,
        table_attributes="class='table'",
        td_attributes="style='width:400px'")
    return render(request, 'view_table.html',
    	{
    	    "table":table,
    	    "title": obj.__dict__.get("name", "Object")
    	 })


from forms import AssayForm
def demo_form(request):
    return render(request, 'assay_form.html',
        {
            "form": AssayForm()
         })

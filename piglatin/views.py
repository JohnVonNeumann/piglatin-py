from django.http import HttpResponse
from django.shortcuts import render

def piglatin_input(request):
    return render(request, 'piglatin_input.html')

def piglatin_output(request):
    return HttpResponse( "u r an" + request.GET['piglatin_input_box'])

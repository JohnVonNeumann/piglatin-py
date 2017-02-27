from django.http import HttpResponse
from django.shortcuts import render

def helloworld(request):
    return render(request, 'piglatin_input.html')

def translation_output(request):
    return render(request, 'piglatin_output.html')

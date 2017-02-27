from django.http import HttpResponse
from django.shortcuts import render

def helloworld(request):
    return render(request, 'piglatin-py/piglatin_input.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')

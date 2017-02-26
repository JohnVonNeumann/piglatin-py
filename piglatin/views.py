from django.http import HttpResponse

def helloworld(request):
    html = "<html><body> Hello, world! </body></html>"
    return HttpResponse(html)

from django.http import HttpResponse

#All functions will receive a request parameter and return an HTTP Response
def home(request):
    return HttpResponse('Hello')
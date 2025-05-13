from django.http import HttpResponse

def index(reguest):
    return HttpResponse('Hello, world. You\'re at the polls index.')
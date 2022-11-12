from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi, this is the home page!")


def userpage(request):
    return HttpResponse("Welcome to the user page")


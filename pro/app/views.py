# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def Home(request):
#     if (request.method=="GET"):
#         return HttpResponse("Hello World")

# def index(request):
#     if (request.method=="GET"):

#         return HttpResponse("This is index page")

#class based



from django.http import HttpResponse
from django.views import View


class home(View):
    def get(self,request):
        return HttpResponse("Hello World")

class index(View):
    def get(self,request):
        return HttpResponse("This is index page")


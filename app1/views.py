from django.shortcuts import render

# Create your views here.
# def home (reqeust):
#     return render(reqeust,'home.html')

def screen (request):
    return render(request, "index.html")

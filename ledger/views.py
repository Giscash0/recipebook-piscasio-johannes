from django.shortcuts import render, HttpResponse

def basicTemplate(request):
    return render(request, '.html')
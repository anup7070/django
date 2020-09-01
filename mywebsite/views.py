

# Views.py
# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    # Get the text
    anup = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowcaps = request.POST.get('lowcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in anup:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif(lowcaps=="on"):
        analyzed=""
        for char in anup:
            analyzed=analyzed + char.lower()

        params = {'purpose': 'change to lowercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif (fullcaps == "on"):
        analyzed = ""
        for char in anup:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'change to UPPERCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif (newlineremover == "on"):
        analyzed = ""
        for char in anup:
            if char !="/n":
                analyzed=analyzed+char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('<h1>Error</h1>-Please tick the box')

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")


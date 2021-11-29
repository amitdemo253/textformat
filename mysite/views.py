from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    removepunc = request.POST.get('removepunc')
    fullcaps = request.POST.get('fullcaps',)
    newlineremover = request.POST.get('newlineremover',)
    extraspaceremover = request.POST.get('extraspaceremover',)
    numberremover = request.POST.get('numberremover')
    text = request.POST.get('text')
    if(removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'analyzed_text': analyzed}
        text = analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'analyzed_text': analyzed}
        text = analyzed
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(text):
            # It is for if a extraspace is in the last of the string
            if char == text[-1]:
                if not(text[index] == " "):
                    analyzed = analyzed + char

            elif not(text[index] == " " and text[index+1] == " "):
                analyzed = analyzed + char

        params = {'analyzed_text': analyzed}
        text = analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        text = analyzed
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'
        for char in text:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'analyzed_text': analyzed}
        text = analyzed    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')

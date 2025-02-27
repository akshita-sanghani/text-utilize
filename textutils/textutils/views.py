from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'akshita', 'place':'mars' }
    return render(request, 'index.html',params)

def analyze(request):
    dtext = request.POST.get("text", "default")
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == 'on':
        punctuations = '''...()-[]{};:'"\,<>./?!@#$%^&*_~'''
        analyzed = ''
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove Punctuations',
            'analyzed_text' : analyzed
        }
        dtext = analyzed

    if (fullcaps == "on"):
        analyzed = ''
        for char in dtext:
                analyzed = analyzed + char.upper()
        params = {
            'purpose': 'Change To Uppercase',
            'analyzed_text': analyzed
        }
        dtext = analyzed

    if (newlineremover == "on"):
        analyzed = ''
        for char in dtext:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
        params = {
            'purpose': 'New Line Remover',
            'analyzed_text': analyzed
        }
        dtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ''
        for index, char in enumerate(dtext):
            if not (dtext[index] == ' ' and dtext[index + 1] == ' '):
                analyzed = analyzed + char
        params = {
            'purpose': 'Extra Space Remover',
            'analyzed_text': analyzed
        }
        dtext = analyzed

    if (charcount == "on"):
        analyzed = len(dtext)
        params = {
            'purpose': 'Character Count',
            'analyzed_text': analyzed
        }

    if (removepunc != 'on' and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please select the opration")

    return render(request, 'analyze.html', params)
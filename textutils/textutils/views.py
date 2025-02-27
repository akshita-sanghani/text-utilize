from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'akshita', 'place':'mars' }
    return render(request, 'index.html',params)

def analyze(request):
    dtext = request.GET.get("text", "default")
    removepunc = request.GET.get('removepunc', 'off')
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
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
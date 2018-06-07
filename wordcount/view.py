from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("This is first")

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    wdictionary = {}
    FT = request.GET['Fulltext']
    wordlist = FT.split()

    for word in wordlist:
        if word in wdictionary:
            wdictionary[word] += 1
        else:
            wdictionary[word] = 1
    return render(request, 'count.html', {'fulltext':FT, 'wcount':len(wordlist), 'wdictionary':wdictionary.items()})

def about(request):
    return render(request, 'about.html')
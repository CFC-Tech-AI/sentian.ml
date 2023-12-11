from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserInput
from .analysis import analyze_sentiment  

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        UserInput.objects.create(text=text)
        sentiment = analyze_sentiment(text)
        return render(request, 'result.html', {'sentiment': sentiment, 'text': text})
    return render(request, 'index.html')


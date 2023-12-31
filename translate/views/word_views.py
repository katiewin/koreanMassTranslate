from django.shortcuts import render
from django.views import View 
from ..models import WordsToTranslate
from django.http import HttpResponseNotAllowed

class Views(View): 
    def get(self, request):
        words = WordsToTranslate.objects.all()
        return render(request, 'vocabList.html', {'words': words})

    def post(self, request):
        return HttpResponseNotAllowed(['GET'])



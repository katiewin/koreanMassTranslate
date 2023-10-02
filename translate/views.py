from django.shortcuts import render
from django.http import HttpResponse
from konlpy.tag import Okt
import numpy as np


def translate(request):
    return render(request, 'textConvertor.html')

def process_text(request):
    if request.method == 'POST':
        text_data = request.POST.get('inputText', '')
        return HttpResponse(f'Successfully received: {breakText(text_data)}')

def breakText(inputText):
    text = inputText
    okt = Okt()
    trans = np.array(okt.pos(text, norm=True, stem=True, join=False))
    trans = np.unique(trans, axis=0)
    return trans


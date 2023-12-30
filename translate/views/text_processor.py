from django.shortcuts import render, redirect
from django.views import View 
from .translator import EnglishToKorean



class TextProcessor(View): 
    def get(self, request):
        return render(request, 'textConvertor.html')

    def post(self, request):
        text_data = request.POST.get('inputText', '')
        translator = EnglishToKorean()
        translator.breakText(text_data)
        return redirect('view_words')

    def process_text(self, request):
        if request.method == 'POST':
            text_data = request.POST.get('inputText', '')
            translator = EnglishToKorean()
            translator.breakText(text_data)
            return redirect('view_words')  

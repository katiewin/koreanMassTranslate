from django.views import View 
from ..models import WordsToTranslate
from django.shortcuts import render, redirect

class buttonConfig(View):

    def delete_item(request, custom_id):
        item = WordsToTranslate.objects.get(custom_id=custom_id)
        item.delete()
        return redirect('view_words')
    
    def delete_all(request):
        WordsToTranslate.objects.all().delete()
        return redirect('view_words')


from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views import View 
from konlpy.tag import Okt
import numpy as np
from ..models import WordsToTranslate
from .api_call import APICall
import logging

logging.basicConfig(level=logging.DEBUG)

class EnglishToKorean(View):
    def get(self, request):
        return render(request, 'vocabList.html')

    def post(self, request):
        text_data = request.POST.get('inputText', '')
        self.breakText(text_data)
        return redirect('view_words')

    def breakText(self, inputText):
        text = inputText
        okt = Okt()
        trans = np.array(okt.pos(text, norm=True, stem=True, join=False))
        trans = np.unique(trans, axis=0)
        self.breakWords(trans) 

    def maping(self, pos):
        english_to_korean_mapping = {
            'Noun': '1',
            'Verb': '5',
            'Adjective': '6',
            'Adverb': '8'
        }

        english_speech_categories = set(english_to_korean_mapping.keys())

        if pos[1] in english_speech_categories:
           translation, example_sentence = APICall.getWords(pos[0], english_to_korean_mapping[pos[1]])
           self.dataBase(pos[0], pos[1], english_to_korean_mapping[pos[1]], translation, example_sentence)
    
    def breakWords(self, trans):
        for pos in trans:
            self.maping(pos)

    
    def dataBase(self, word, epos, kpos, e_translation, e_sentence):
        try:
            existing_word = WordsToTranslate.objects.filter(k_word=word, kpos=kpos).first()

            if existing_word is not None:
                return

            words_translate = WordsToTranslate()
            words_translate.k_word = word
            words_translate.epos = epos
            words_translate.kpos = kpos
            words_translate.e_translation = e_translation
            words_translate.e_sentence = e_sentence

            words_translate.save()

        except IntegrityError:
            pass


from django.db import models


class WordsToTranslate(models.Model):
    k_word = models.CharField(max_length=50)
    kpos = models.CharField(max_length=20)
    epos = models.CharField(max_length=20)
    e_translation = models.CharField(max_length=50)
    e_sentence = models.CharField(max_length=100)









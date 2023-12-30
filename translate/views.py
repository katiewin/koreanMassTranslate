from django.shortcuts import render, redirect
from konlpy.tag import Okt
import numpy as np
from django.db import IntegrityError
from .models import WordsToTranslate
from django.views import View 
from django.http import HttpResponseNotAllowed

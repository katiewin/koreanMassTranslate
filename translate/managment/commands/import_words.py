import pandas as pd
from django.core.management.base import BaseCommand
from translate.models import WordsToTranslate


class Command(BaseCommand):
    help = 'Import words into WordsToTranslate model'

    def handle(self, *args, **options):
        excel_files = ['koreanMassTranslate\media\excel_folder\1_30000_20231201.xls', 'koreanMassTranslate\media\excel_folder\2_30000_20231201.xls', 'koreanMassTranslate\media\excel_folder\3_14935_20231201.xls']

        for excel_file in excel_files:
            df = pd.read_excel(excel_file)

    
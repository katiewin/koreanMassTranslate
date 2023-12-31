from django.contrib import admin
from django.urls import path
from homePage import views as home_page_views 
from translate.views.text_processor import TextProcessor
from translate.views.translator import EnglishToKorean
from translate.views.word_views import Views
from translate.views.button_config import buttonConfig
from translate.views.add_word import AddWordView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page_views.home),
    path('process-text/', EnglishToKorean.as_view(), name='process_text'),
    path('translate/', TextProcessor.as_view(), name='translate'),
    path('view-words/', Views.as_view(), name='view_words'),
    path('delete-item/<int:custom_id>/', buttonConfig.delete_item, name='delete-item'),
    path('delete-all', buttonConfig.delete_all, name='delete-all'),
    path('add-word/', AddWordView.as_view(), name='add-word'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
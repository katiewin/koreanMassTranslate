from django.contrib import admin
from django.urls import path
from translate import views as translate_views
from homePage import views as home_page_views 
from translate.views.text_processor import TextProcessor
from translate.views.translator import EnglishToKorean
from translate.views.word_views import Views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page_views.home),
    path('process-text/', EnglishToKorean.as_view(), name='process_text'),
    path('translate/', TextProcessor.as_view(), name='translate'),
    path('view-words/', Views.as_view(), name='view_words'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
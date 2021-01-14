from django.contrib import admin
from django.urls import path

from projeto.views.view_chatbot import bot, get_response
from projeto.views.view_digit import digits
from projeto.views.view_shapes import shape
from projeto.views.view_home import home, jogo_cores, tente_vc, jogos, videos, jogo_animals, tente_vc_animals, fale_conosco, corpoHumano, casa

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', bot, name='bot'),
    path('bot/get-response/', get_response),
    path('digit/', digits, name='digit'),
    path('', home, name='home'),
    path('cores', jogo_cores, name='cores'),
    path('tente_vc', tente_vc, name='tente_vc'),
    path('jogos', jogos, name='jogos'),
    path('shapes/', shape, name='shape'),
    path('videos/', videos, name='videos'),
    path('jogo_animals/', jogo_animals, name='jogo_animals'),
    path('tente_vc_animals/', tente_vc_animals, name='tente_vc_animals'),
    path('fale_conosco/', fale_conosco, name='fale_conosco'),
    path('corpoHumano/', corpoHumano, name='corpoHumano'),
    path('casa/', casa, name='casa'),
]

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
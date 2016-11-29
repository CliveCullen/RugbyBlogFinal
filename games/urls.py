from django.conf.urls import url, include
from games import views as game_views
urlpatterns = [
    url(r'^head_to_head/$',game_views.head_to_head, name='head_to_head'),
]


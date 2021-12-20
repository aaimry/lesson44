from django.urls import path

from game.views import index_view, score_view

urlpatterns = [
    path('', index_view),
    path('score/', score_view)

]
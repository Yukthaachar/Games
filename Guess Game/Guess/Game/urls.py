from django.urls import path
from .views import Game
urlpatterns=[
    path("Game/",Game,name="Game")
]
from django.urls import path
from .views import MovieList,MovieDetail

urlpatterns = [
    path('list/',MovieList.as_view()),
    path('<int:pk>/',MovieDetail.as_view())
]

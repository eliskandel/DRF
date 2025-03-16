from django.urls import path
from .views import WatchListView,WatchListDetailView,PlatformView,PlatformDetailView

urlpatterns = [
    path('list/',WatchListView.as_view()),
    path('list/<int:pk>/', WatchListDetailView.as_view()),
    path('platform/', PlatformView.as_view()),
    path('platform/<int:pk>/',PlatformDetailView.as_view())
]

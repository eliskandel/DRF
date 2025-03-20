from django.urls import path
from .views import WatchListView,WatchListDetailView,PlatformView,PlatformDetailView,ReviewListView,ReviewCreateView

urlpatterns = [
    path('watchlist/',WatchListView.as_view()),
    path('watchlist/<int:pk>/', WatchListDetailView.as_view()),
    path('platform/', PlatformView.as_view()),
    path('platform/<int:pk>/',PlatformDetailView.as_view()),
    path('watchlist/<int:pk>/review/',ReviewListView.as_view()),
    # path('watchlist/<int:pk>/review/',ReviewDetailView.as_view()),
    path('watchlist/<int:pk>/review-create/',ReviewCreateView.as_view())
]

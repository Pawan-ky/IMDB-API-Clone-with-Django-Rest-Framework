from django.urls import path,include
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV
# from watchlist_app.api.views import movie_list,movie_detail

urlpatterns = [
    # function based view urls
    # path("list/",movie_list,name="movie_list"),
    # path('<int:pk>',movie_detail,name="movie_detail"),

    path("list/",WatchListAV.as_view(),name="movie_list"),
    path('<int:pk>',WatchDetailAV.as_view(),name="movie_detail"),
    path("stream/",StreamPlatformAV.as_view(),name="stream"),
    path("stream/<int:pk>",StreamPlatformDetailAV.as_view(),name="stream_detail"),
]
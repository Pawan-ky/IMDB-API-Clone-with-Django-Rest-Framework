from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import (WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV,
                                    # ReviewListGV,ReviewDetailGV
                                    ReviewListGCV,ReviewDetailGCV,ReviewCreateGCV,UserReviewList,WatchListGV
                                    # StreamPlatformViewsSet
                                    )

# router = DefaultRouter()
# router.register("stream",StreamPlatformViewsSet,basename='streamplatform')

urlpatterns = [
    # function based view urls
    # path("list/",movie_list,name="movie_list"),
    # path('<int:pk>',movie_detail,name="movie_detail"),

    #  class based views
    path("list/",WatchListAV.as_view(),name="movie_list"),
    path('<int:pk>/',WatchDetailAV.as_view(),name="movie_detail"),
    
    # filtering/ordering/search
    path('list2/',WatchListGV.as_view(),name="movie_detail"),

    # w/o viewsets
    path("stream/",StreamPlatformAV.as_view(),name="stream"),
    path("stream/<int:pk>/",StreamPlatformDetailAV.as_view(),name="stream_detail"),
    # with viewsets
    # path('',include(router.urls)),

    # genericsViews and mixins
    # path("review/",ReviewListGV.as_view(),name="review-list"),
    # path("review/<int:pk>",ReviewDetailGV.as_view(),name="review-detail"),

    #  generic concrete class views used
    path("<int:pk>/review-create/",ReviewCreateGCV.as_view(),name="review-create"),
    path("<int:pk>/reviews/",ReviewListGCV.as_view(),name="review-list"),
    path("review/<int:pk>/",ReviewDetailGCV.as_view(),name="review-detail"),
    
    path("review/<str:username>/",UserReviewList.as_view(),name="User-review-detail")

]
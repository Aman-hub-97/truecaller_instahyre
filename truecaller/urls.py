from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

#router= DefaultRouter()
#router.register('search',views.SearchList,basename='search')

urlpatterns=[
    path('profile/',views.HomeApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('search/',views.UserHome.as_view()),
    path('search/<int:pk>',views.SearchList.as_view())
    #path('',include(router.urls))
]
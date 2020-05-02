from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('profiles', views.UserProfileViewSet)
router.register('feeds', views.UserProfileFeedViewSet)

urlpatterns = [
    path('greet/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
    path('test/<int:t_id>', views.test, {"id":23})
]

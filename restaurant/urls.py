from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = DefaultRouter()
router.register('tables', views.BookingViewSet, basename='table')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-items-detail'),
    path('api-token-auth/', obtain_auth_token),
] + router.urls
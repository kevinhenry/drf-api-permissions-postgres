from django.urls import path
from .views import KitList, KitDetail

urlpatterns = [
    path('', KitList.as_view(), name='post_list'),
    path('<int:pk>/', KitDetail.as_view(), name='post_detail')
]
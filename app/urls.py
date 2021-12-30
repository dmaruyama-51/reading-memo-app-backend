from django.urls import path 
from app import views 

urlpatterns = [
    path('list/', views.ReadingMemoList.as_view(), name='list'),
    path('list/<int:pk>/', views.ReadingMemoListDetail.as_view(), name='list-detail'),
    path('create/', views.ReadingMemoCreate.as_view(), name='create'),
    path('update/<int:pk>', views.ReadingMemoUpdate.as_view(), name='update'),
    path('destroy/<int:pk>', views.ReadingMemoDestroy.as_view(), name='destroy')
]
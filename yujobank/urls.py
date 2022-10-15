from django.urls import path
from . import views

app_name = 'yujobank'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('yujobank/create/', views.DiaryCreateView.as_view(), name='diary_create'),
    path('yujobank/create/complete/', views.DiaryCreateCompleteView.as_view(), name='diary_create_complete'),
    path('list/', views.DiaryListView.as_view(), name='diary_list'),
    path('yujobank/detail/<uuid:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('yujobank/update/<uuid:pk>/', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('yujobank/delete/<uuid:pk>/', views.DiaryDeleteView.as_view(), name='diary_delete'),
]
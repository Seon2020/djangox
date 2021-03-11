from django.urls import path
from .views import StrainCreateView, StrainDeleteView, StrainListView, StrainUpdateView, StrainDetailView

urlpatterns = [
    path('', StrainListView.as_view(), name='strain_list'),
    path('<int:pk>/', StrainDetailView.as_view(), name='strain_detail'),
    path('create/', StrainCreateView.as_view(), name='strain_create'),
    path('<int:pk>/update/', StrainUpdateView.as_view(), name='strain_update'),
    path('<int:pk>/delete/', StrainDeleteView.as_view(), name='strain_delete')
]
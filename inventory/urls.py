from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('base/', views.BaseInventoryView.as_view(), name='base-inventory'),
    path('adjustments/', views.StockAdjustmentListView.as_view(), name='adjustment-list'),
    path('adjustments/create/', views.StockAdjustmentCreateView.as_view(), name='adjustment-create'),
    path('adjustments/<int:pk>/', views.StockAdjustmentDetailView.as_view(), name='adjustment-detail'),
]
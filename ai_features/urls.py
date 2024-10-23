from django.urls import path
from . import views

urlpatterns = [
    path('view-sales-history/', views.view_sales_history, name='view_sales_history'),
    path('view-open-sales/', views.view_open_sales, name='view_open_sales'),
    path('cash-in-out/', views.cash_in_out, name='cash_in_out'),
    path('end-of-day/', views.end_of_day, name='end_of_day'),
    path('feedback-analysis/', views.feedback_analysis, name='feedback_analysis'),
]

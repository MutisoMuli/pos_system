from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get current date
        today = timezone.now()
        
        # Add dashboard data to context
        context.update({
            'top_products': Product.objects.annotate(
                sales_count=Count('orderitem')
            ).order_by('-sales_count')[:5],
            
            'total_sales': Product.objects.aggregate(
                total=Sum('orderitem__total_price')
            )['total'] or 0.00,
            
            # Add more context data as needed
        })
        
        return context
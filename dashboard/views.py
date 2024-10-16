from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from django.utils import timezone

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get current date
        today = timezone.now()
        
        # Add dashboard data to context (excluding order items)
        context.update({
            # Get the top 5 products by stock quantity for now (you can change this to any other metric)
            'top_products': Product.objects.order_by('-selling_price')[:5],
            
            # Since we are removing total sales, you can remove this or add a placeholder
            'total_sales': 0.00,
            
            # Add more context data as needed
        })
        
        return context

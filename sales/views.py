from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product

class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'sales/sales.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
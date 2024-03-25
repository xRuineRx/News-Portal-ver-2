from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, News_All
from datetime import datetime
# Create your views here.

class ProductsList(ListView):
    model = Product
    ordering = 'name'

    # queryset= Product.objects.filter(
    #     price__lt = 100
    # ).order_by(
    #     'name'
    # )

    template_name = 'flatpages/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Жестко продаем и еще поем !"
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'flatpages/product.html'
    context_object_name = 'product'

class PostList(ListView):
    model = News_All
    ordering = '-time_in'

    template_name = 'flatpages/News_all.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Хорошие новости !"
        return context

class PostDetail(DetailView):
    model = News_All
    pk_url_kwarg = 'id'

    template_name = 'flatpages/News_all_post.html'
    context_object_name = "news"

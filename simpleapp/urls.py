from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList, ProductDetail,PostList,PostDetail

urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('News_all', PostList.as_view()),
    path('News_all/<int:id>', PostDetail.as_view()),
]
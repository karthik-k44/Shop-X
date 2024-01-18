from django.urls import path
from Store import views
urlpatterns=[
    path('Categories/',views.Home.as_view(),name="home"),
    path('register/',views.Register.as_view(),name="reg"),
    path('Products/<int:pk>/',views.ProductView.as_view(),name="product"),
    path('Details/<int:pk>',views.Product_detail.as_view(),name="details")
]

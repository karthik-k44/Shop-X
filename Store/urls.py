from django.urls import path
from Store import views
urlpatterns=[
    path('home/',views.Home.as_view(),name="home"),
    path('register/',views.Register.as_view(),name="reg"),
    path('prod/<int:pk>/',views.ProductView.as_view(),name="product")
]

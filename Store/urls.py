from django.urls import path
from Store import views
urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('register/',views.Register.as_view(),name="reg"),
    path('Products/<int:pk>/',views.ProductView.as_view(),name="product"),
    path('Details/<int:pk>',views.Product_detail.as_view(),name="details"),
    path('reg/',views.Register.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="signin"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('Cart/<int:id>',views.AddcartView.as_view(),name="addcart"),
    path('Cardetail/',views.CartdetailView.as_view(),name="details"),
    path('deletecart/<int:id>',views.Cartdelete.as_view(),name="delete"),
    path('ordernow/<int:id>',views.OrderView.as_view(),name="order")
]

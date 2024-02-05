from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from Store.models import Category,Product,Cart,Order
from Store.forms import RegisterForm,LoginForm,OrderForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

# Create your views here.

class Home(ListView):
    model=Category
    template_name="store/index.html"
    context_object_name="categories"  
    
class Register(CreateView):
    template_name="store/reg.html"
    form_class =RegisterForm
    model=User
    success_url=reverse_lazy("signin")
    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        form=LoginForm()
        return render(request, "store/login.html",{"form":form})
    
    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request, username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
            else:
                print("invalid creds")
        else:
            print("..")
        return render(request, "store/login.html", {"form":form})    
    
    

class ProductView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(category__id=id)
        name=Category.objects.get(id=id)
        return render(request,"store\category_detail.html",{"data":data,"name":name})
    
class Product_detail(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(id=id)
        return render(request, "store/p_detail.html",{"data":data})

class LogoutView(View):
    def get(self, request,*args,**kwargs):
        logout(request)
        return redirect("home")
    
class AddcartView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        data=Product.objects.get(id=id)
        Cart.objects.create(item=data,User=request.user)
        return redirect("details")
 
class Cartdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Cart.objects.get(id=id).delete()
        return redirect("details")
    
class CartdetailView(View):
    def get(self,request,*args,**kwargs):
        data=Cart.objects.filter(User=request.user)
        return render(request,"store\cart.html",{"data":data})

class OrderView(View):
    def get(self, request, *args, **kwargs):
        form=OrderForm
        return render(request,"store/order.html",{"form":form})
    def post(self, request, *args, **kwargs):
        id=kwargs.get("id")
        data=Product.objects.get(id=id)
        form=OrderForm(request.POST)
        if form_is.valid():
            qs=form.cleaned_data.get("address")
            order.objects.create(order_item=data, customer=request.user,  address=qs)
            return redirect("home")
        return redirect("cart")
    
class OrderListView(View):
    def get(self, request, *args, **kwargs):
        data=order.objects.filter(customer=request.user)
        return render(request,"store/vieworder.html",{"data":data})
    
class RemoveOrder(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        order.objects.get(id=id).delete()
        return redirect("cart")
    
    
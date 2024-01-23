from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from Store.models import Category,Product
from Store.forms import RegisterForm,LoginForm
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
    
 
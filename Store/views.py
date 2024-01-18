from django.shortcuts import render
from django.views.generic import View,ListView
from Store.models import Category,Product

# Create your views here.

class Home(ListView):
    model=Category
    template_name="store/index.html"
    context_object_name="categories"  
    
class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request,"store\reg.html")   
    
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
    
 
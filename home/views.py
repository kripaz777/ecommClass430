from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['new_products'] = Product.objects.filter(label = 'new',stock = 'In stock')
        self.views['hot_products'] = Product.objects.filter(label = 'hot',stock='In stock')
        self.views['sale_products'] = Product.objects.filter(label = 'sale',stock= 'In stock')

        return render(request,'index.html',self.views)
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()
    views['sale_products'] = Product.objects.filter(label='sale', stock='In stock')


class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['new_products'] = Product.objects.filter(label = 'new',stock = 'In stock')
        self.views['hot_products'] = Product.objects.filter(label = 'hot',stock='In stock')

        return render(request,'index.html',self.views)

class CategoryView(BaseView):
    def get(self,request,slug):
        ids = Category.objects.get(slug = slug).id
        cat_name = Category.objects.get(slug = slug).name
        print(cat_name,ids)
        self.views['cat_product'] = Product.objects.filter(category_id = ids)
        print(self.views['cat_product'])
        return render(request,'category.html',self.views)


class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('query')
        if query != '':
            self.views['search_product'] = Product.objects.filter(name__icontains = query)
        else:
            return redirect('/')
        return render(request,'search.html',self.views)


class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.views['product_detail'] = Product.objects.filter(slug = slug)
        subcat_id = Product.objects.get(slug = slug).subcategory_id
        product_id = Product.objects.get(slug = slug).id
        self.views['product_image'] = ProductImage.objects.filter(product_id=product_id)
        self.views['subcat_product'] = Product.objects.filter(subcategory_id=subcat_id)
        return render(request, 'product-detail.html', self.views)
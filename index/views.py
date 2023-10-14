from django.shortcuts import render, redirect
from . import forms, models
from . models import Product
from . forms import ProductForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar,
               'products': products,
               'categories': categories}
    return render(request, 'index.html', context)

def news_home(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar,
               'products': products,
               'categories': categories}
    return render(request, 'news_home.html', context)

def about(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar,
               'products': products,
               'categories': categories}
    return render(request, 'about.html', context)

def contacts(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar,
               'products': products,
               'categories': categories}
    return render(request, 'contacts.html', context)

def get_exact_category(request, pk):
    category = models.Category.objects.get(id=pk)
    products = models.Product.objects.filter(product_category=category)
    context = {'products': products}
    return render(request, 'exact_category.html', context)

def get_exact_product(request, pk):
    product = models.Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'exact_product.html', context)

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = models.Product.objects.get(product_name__icontains=get_product)
            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')

def register(request):
    error = ''
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm(request.POST)
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
    form = ProductForm()
    data = {'form': form, 'error': error}
    return render(request, 'create.html', data)

class NewsUpdateView(UpdateView):
    model = Product
    template_name = 'create.html'
    form_class = ProductForm

class NewsDeleteView(DeleteView):
    model = Product
    success_url = '/news_home'
    template_name = 'news-delete.html'



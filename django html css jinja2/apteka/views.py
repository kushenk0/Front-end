from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'apteka/index.html')

def about(request):
    return render(request, 'apteka/about.html')

def contact(request):
    return render(request, 'apteka/contact.html')

def products(request):
    return render(request, 'apteka/products.html')

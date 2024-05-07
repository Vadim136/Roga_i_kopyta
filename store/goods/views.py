from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.models import Products

from goods.utils import q_search


# Create your views here.
def catalog(request, category_slug = None):

    order_by = request.GET.get('order_by',None)
    price_sort = request.GET.get('price_sort',None)
    query = request.GET.get('q',None)

    if category_slug=='all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if price_sort == '' and order_by and order_by != 'default':
        goods = goods.order_by(order_by)
    elif price_sort and order_by =='-price' and order_by != 'default':
        goods = goods.filter(price__gte=price_sort).order_by(order_by)
    elif price_sort and order_by =='price' and order_by != 'default':
        goods = goods.filter(price__lte=price_sort).order_by(order_by)




    context = {
        "title": "Roga&Kopyta - Каталог",
        "goods": goods,
        "slug_url": category_slug
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):


    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product ,
        
    }



    return render(request, "goods/product.html", context=context)

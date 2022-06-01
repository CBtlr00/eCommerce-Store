from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from .models import Category, Product, Review, Address

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'shop/user/signup.html', {'form': form}) 

@login_required
def myaccount(request):
    return render(request, 'shop/account/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('shop:myaccount')
    return render(request, 'shop/account/edit_myaccount.html')

@login_required
def myaddress(request):
    return render(request, 'shop/account/myaddress.html')

@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "shop/account/user_wish_list.html", {"wishlist": products})

@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, product.name + " has been removed from your WishList")
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, "Added " + product.name + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def edit_address(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone = request.POST.get('phone')
        user.country = request.POST.get('country')
        user.address_line = request.POST.get('address_line')
        user.address_line2 = request.POST.get('address_line2')
        user.town_city = request.POST.get('town_city')
        user.postcode = request.POST.get('postcode')
        user.save()

        return redirect('shop:myaccount')
    return render(request, 'shop/account/myaddress.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products=Product.objects.filter(category=product.category).exclude(id=id)[:4]
    cart_product_form = CartAddProductForm()
    if request.method == 'POST':
        rate = request.POST.get('rate', 0)
        comment = request.POST.get('comment', '')

        if comment:
            reviews = Review.objects.filter(user=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rate = rate
                review.comment = comment
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rate=rate,
                    comment=comment,
                    user=request.user
                )

            return redirect(product, id=id, slug=slug)

    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form ,'related':related_products})
    

def search(request):
    if request.method == 'GET':
        k = request.GET.get('k')
        if k:
            products = Product.objects.filter(name__icontains=k) 
            return render(request, 'shop/product/search.html', {'products':products})
        else:
            print("No information to show")
            return render(request, 'shop/product/search.html', {})







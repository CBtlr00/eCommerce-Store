from django.contrib.auth import views
from django.urls import path, reverse_lazy

from shop.views import product_list, product_detail, signup, myaccount, edit_myaccount, search, add_to_wishlist, wishlist, myaddress
app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='shop/user/login.html'), name='login'),
    path('change_password/', views.PasswordChangeView.as_view(template_name='shop/user/change_password.html', success_url=reverse_lazy('password_change_done')), name='password_change'),
    path('password_change_done/', views.PasswordChangeDoneView.as_view(template_name='shop/user/password_change_done.html'), name='password_change_done'),
    path('reset_password', views.PasswordResetView.as_view(template_name='shop/user/reset_password.html', success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(template_name='shop/user/password_reset_done.html'), name='password_reset_done'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('search', search, name='search'),
    path('wishlist/add_to_wishlist/<int:id>', add_to_wishlist, name='user_wishlist'),
    path("myaccount/wishlist", wishlist, name="wishlist"),
    path("myaccount/myaddress", myaddress, name="myaddress"),

]
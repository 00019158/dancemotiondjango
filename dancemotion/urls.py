from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from shop.views import (
    index,
    products_api,
    create_order,
    order_success,
    register,
)

urlpatterns = [
    # Main page
    path("", index, name="home"),

    # Auth
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", register, name="register"),

    # Orders
    path("order/create/", create_order, name="create_order"),
    path("order/success/", order_success, name="order_success"),

    # API
    path("api/products/", products_api, name="products_api"),

    # Admin panel
    path("admin/", admin.site.urls),
]

# Static + media (only in DEBUG)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

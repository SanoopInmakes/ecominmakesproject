from . import views
from django.urls import path

app_name='shop'

urlpatterns = [

    path('',views.allProductCat,name='allProductCat'),
    path('shop/<slug:c_slug>/',views.allProductCat,name='products_by_category'),
    path('shop/<slug:c_slug>/<slug:product_slug>/',views.ProDetails,name='Product_Category_Details'),
    ]
# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapi.views import ProductView, ItemView, BuyerView,RegisterView,LoginAPIView,BuyerDetail,BuyerTransactionCreateView, UpdateBuyerProfileAPIView, DepositToMainBalance, TransferToCashupDeposit, TransferToCashupOwingDeposit, PurchaseProduct,ConfirmedProductsList,CashupOwingDepositByBuyerAPIView,CashupDepositByBuyerAPIView,ConfirmedBuyersForProducts,BuyerPurchasesAPIView , ConfirmedBuyerView,ProductDetail, CartedProductsList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
from django.contrib.auth.models import User

admin.site.site_header= 'CashUp'
admin.site.index_title='Welcome to Cashup'



# Create a default router and register your viewsets
router = DefaultRouter()
router.register(r'purchase', ProductView)
router.register(r'buyers', BuyerView)
router.register(r'items', ItemView)


# Define the urlpatterns with the additional views included
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/confirmed-products/', ConfirmedProductsList.as_view(), name='confirmed-products'),
    path('api/carted-products/', CartedProductsList.as_view(), name='carted-products'),
    path('api/product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
     path('api/confirmed-buyers/', ConfirmedBuyerView.as_view(), name='confirmed-buyer'),
     path('api/confirmed-buyersforproduct/', ConfirmedBuyersForProducts.as_view(), name='confirmed-buyersforproduct'),
     path('api/buyer-purchases/<int:buyer_id>/', BuyerPurchasesAPIView.as_view(), name='buyer-purchases'),
     path('api/cashup-deposit/<int:buyer_id>/', CashupDepositByBuyerAPIView.as_view(), name='cashup-deposit'),
     path('register/', RegisterView.as_view(), name='register'),
     path('login/', LoginAPIView.as_view(), name='login'),
    path('update-profile/', UpdateBuyerProfileAPIView.as_view(), name='update-profile'),
    path('deposit/<int:buyer_id>/', DepositToMainBalance.as_view(), name='deposit-to-main-balance'),
    path('transfer-to-cashup-deposit/<int:buyer_id>/', TransferToCashupDeposit.as_view(), name='transfer-to-cashup-deposit'),
    path('transfer-to-cashup-owing-deposit/<int:buyer_id>/', TransferToCashupOwingDeposit.as_view(), name='transfer-to-cashup-owing-deposit'),
    path('purchase/', PurchaseProduct.as_view(), name='purchase-product'),
    path('api/cashup-owing-deposit/<int:buyer_id>/', CashupOwingDepositByBuyerAPIView.as_view(), name='cashup-owing-deposits-by-buyer'),
    path('api/buyer/<int:pk>/', BuyerDetail.as_view(), name='buyer-detail'),
    path('buyer_transactions/', BuyerTransactionCreateView.as_view(), name='buyer_transaction_create')
     
    
]
     


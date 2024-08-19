from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from shop.views import CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, AddressViewSet
from shop import views

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('categories/', views.CategoryList.as_view(), name='categories-list'),
    # path('categories/create/', views.CategoryCreate.as_view(), name='categories-create'),
    # path('categories/<int:pk>/detail', views.CategoryDetail.as_view(), name='categories-detail'),
    # path('categories/<int:pk>/update', views.CategoryUpdate.as_view(), name='categories-update'),
    # path('categories/<int:pk>/delete', views.CategoryUpdate.as_view(), name='categories-update'),
    # path('categories/<int:pk>/', views.CategoryDetailUpdateDelete.as_view(), name='categories-detail-update-delete'),
    # path('my-categories/', views.CategoryMixinView.as_view(), name='my-category'),
    # path('my-categories/create', views.CategoryListCreateMixinView.as_view(), name='my-category-create'),
    # path('my-categories/<int:pk>/update/', views.CategoryUpdateMixinView.as_view(), name='my-category-update'),
    path('api/categories/', views.CategoryListCreateMixin.as_view(), name='category-list-create'),
    # re_path(r'^api/categories/(?P<title>.+)/$', views.CategoryListFilter.as_view(), name='category-list-filter'),
    # path('api/categories', views.CategoryListFilter.as_view(), name='category-list-filter'),
    path('api/categories/<int:pk>/', views.CategoryRetrieveUpdateDeleteMixin.as_view(),
         name='category-detail-update-delete'),
    path('api/pictures/', views.PictureListMixinView.as_view(), name='picture-list')

]

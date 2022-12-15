from django.urls import path
from .views import CollectionList, CollectionDetail, CollectionCreate, CollectionUpdate, CollectionDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', CollectionList.as_view(), name='collection')
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', CollectionList.as_view(), name='collections'),
    path('collection/<int:pk>/', CollectionDetail.as_view(), name='collection'),
    path('collection-create/', CollectionCreate.as_view(), name='collection-create'),
    path('collection-update/<int:pk>/', CollectionUpdate.as_view(), name='collection-update'),
    path('collection-delete/<int:pk>/', CollectionDelete.as_view(), name='collection-delete'),
]
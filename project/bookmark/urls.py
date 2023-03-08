from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('<int:pk>/', EditBookmark.as_view(), name='update_view'),
    path('delete/<bookmark_id>', delete_post, name='delete'),
    path('delete_category/<category_id>', delete_category, name='delete_category'),
    path('create/', CreateCategory.as_view(), name='create_category'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_view'),
]

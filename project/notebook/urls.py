from django.urls import path
from .views import *

urlpatterns = [
    path('', MainNotebook.as_view(), name='notebook_main'),
    path('<int:pk>/', DetailNotebook.as_view(), name='notebook_detail'),
    path('create/', CreateNotebook.as_view(), name='notebook_create'),
    path('delete/<int:pk>', DeleteNotebook.as_view(), name='notebook_delete'),
    path('edit/<int:pk>', EditNotebook.as_view(), name='notebook_edit'),
]

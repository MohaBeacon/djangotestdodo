from .views import TodoCreate,Update,Delete
from django.urls import path

urlpatterns = [

    path('', TodoCreate.as_view(), name="create"),
    path('<pk>/update', Update.as_view(), name="update"),
    path('<pk>/delete', Delete.as_view(), name="delete"),
]
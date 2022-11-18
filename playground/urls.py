import re
from django.urls import re_path
from . import views

urlpatterns = [
    re_path("item", views.item),
    re_path("action/<int:pk>", views.action)
]
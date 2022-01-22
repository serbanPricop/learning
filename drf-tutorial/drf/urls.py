from os import name
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('bicycle/', views.bicyle_list, name='bicycle_list'),
    path('bicycle/<int:pk>', views.bicycle_detail, name='bicycle_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
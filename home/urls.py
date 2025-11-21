from django.urls import path

from home.views import *

urlpatterns = [

    path('', index_view, name="index"),
    path('blog', blog_view, name='blog'),
    path('single',single_view, name='single'),

]
from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('quote/', views.quote, name='quote'),
    path('tag/', views.tag, name='tag'),  
    path('detail/<int:quote_id>', views.detail, name='detail'),  
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),
    path('author/', views.author, name='author'),   
    path('author_detail/<int:author_id>', views.author_detail, name='author_detail'),          
]
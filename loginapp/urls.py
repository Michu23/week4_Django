from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.base, name='cards'),
    path('login/',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('',views.ultimate,name='ultimate'),
    path('logout/',views.logout,name='ultimate'),
    
    
]
from django.urls import path
from  . import  views

urlpatterns=[
  	path('', views.home , name="home"),
    path('contact/', views.contact , name="contact"),
    path('contact_form_data/', views.contact_form_data, name="contact_form_data"),
    path('login/', views.login_view, name='login'),
		path('contact_form_data/', views.contact_form_data, name="contact_form_data"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout_view'),
    path('detail_view/<int:id>/', views.detail_view, name='detail_view'),
]
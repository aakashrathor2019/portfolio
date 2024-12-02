from django.urls import path
from  . import  views

urlpatterns=[
		path('core/contact_form_data/',views.contact_form_data,name="contact_form_data") 
]
from django.urls import path
from  . import views

urlpatterns=[
		path('skill/',views.skill,name='skill'),
    path('update_skills/',views.update_skills,name="update_skills"),
    path('add_certifications/',views.add_certifications,name="add_certifications"),
    path('add_experience/',views.add_experience,name="add_experience"),
    path('add_work_experience/',views.add_work_experience,name="add_work_experience"),
]
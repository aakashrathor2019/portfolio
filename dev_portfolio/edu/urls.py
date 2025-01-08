from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  . import views

urlpatterns=[
		path('skill/',views.skill,name='skill'),
    path('update_skills/',views.update_skills,name="update_skills"),
    path('add_certifications/',views.add_certifications,name="add_certifications"),
    path('add_experience/',views.add_experience,name="add_experience"),
    path('add_work_experience/',views.add_work_experience,name="add_work_experience"),
    path('update_resume/', views.update_resume, name="update_resume"),
    path('download_resume/', views.download_resume, name='download_resume'),
    path('view_resume/', views.view_resume, name="view_resume"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
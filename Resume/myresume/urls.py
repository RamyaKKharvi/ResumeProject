from django.urls import path
from resume import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('project/', views.project, name='project'),
    path('certificate/', views.certificate, name='certificate'),
    path('contact/', views.contact, name='contact'),
]
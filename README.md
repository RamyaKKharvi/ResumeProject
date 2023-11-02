# ResumeProject
Project to build a resume

### Requirements:
* Python 3.10.12
* Django 4.2.3

### Steps to run this project:
1. Install requirements using `pip install -r requirements.txt` command.
2. Start new project using `django-admin startproject Resume` command.
3. Change directory to django project `cd Resume`
4. Start django application using command `python manage.py startapp myresume`
5. Add app name to setting.py file of django project in INSTALLED_APP
6. Create templates for home page, education details, project details, skills, contacts, and certificates.
7. Write view functions for each template in view.py file and render these templates.
8. Write urlpatterns for Resume project in urls.py file of django project. 
9. Include applications url.py file inside Project url.py file and write urlpatterns for each view functions. 
10. Run server `python manage.py runserver`
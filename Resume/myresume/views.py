from django.shortcuts import render


def home(request):
    active = {'home': 'active'}
    return render(request, 'resume_template/home.html', active)


def education(request):
    active = {'education': 'active'}
    return render(request, 'resume_template/education.html', active)


def skills(request):
    active = {'skills': 'active'}
    return render(request, 'resume_template/skills.html', active)


def project(request):
    active = {'project': 'active'}
    return render(request, 'resume_template/project.html', active)


def certificate(request):
    active = {'certificate': 'active'}
    return render(request, 'resume_template/certificate.html', active)


def contact(request):
    active = {'contact': 'active'}
    return render(request, 'resume_template/contact.html', active)

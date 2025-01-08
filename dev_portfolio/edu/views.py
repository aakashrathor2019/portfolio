from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, Http404
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import SuspiciousFileOperation
from django.core.files.storage import FileSystemStorage
from core.models import Skill, Certifications, Experience, Work_Experience, Resume


# Create your views here.
def skill(request):
  skill_data = Skill.objects.all()
  cert_data = Certifications.objects.all()
  exp_data = Experience.objects.all()
  work_exp_data = Work_Experience.objects.all().order_by('-id')
  resume_data = Resume.objects.last()
  context = {
      'skill': 'active',
      'skill_data': skill_data,
      'cert_data': cert_data,
      'exp_data': exp_data,
      'work_exp_data': work_exp_data,
      'resume_data': resume_data,
    }
  print(skill_data)
  return render(request, 'edu/skill.html', context)

@login_required(login_url='login')
def update_skills(request):
  if request.method == "POST":
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    print('inide update skills function')
    existing_data = Skill.objects.filter(name=name).first()
    print('value of data:', existing_data)
    if name and desc:
      if not existing_data:
        print('Name and Proficiency:', name, desc)
        Skill.objects.create(name=name, desc=desc)
        return redirect('skill')
      else:
        print('inside else', existing_data)
        existing_data.name = name
        existing_data.desc = desc
        existing_data.save()
        return redirect('skill')
    else:
      return render(request, "edu/update_skills.html", {
        'error': 'Please enter valid data...'
      })
  return render(request, "edu/update_skills.html")


@login_required(login_url='login')
def add_certifications(request):
  if request.method == "POST":
    cert_name = request.POST.get('cert_name')
    cert_duration = request.POST.get('cert_duration')
    cert_from = request.POST.get('cert_from')
    print('DATA:', cert_duration, cert_from, cert_name)

    if cert_duration and cert_from and cert_name:
      Certifications.objects.create(
        cert_name=cert_name, cert_duration=cert_duration, cert_from=cert_from)
      return redirect('skill')
    else:
      return render(
        request, "edu/add_certifications.html", {
          'errors': "Invalid Data....please add valid data"
        })
  return render(request, "edu/add_certifications.html")


@login_required(login_url='login')
def add_experience(request):
  if request.method == "POST":
    prj_name = request.POST.get('prj_name')
    prj_link = request.POST.get('prj_link')
    prj_desc = request.POST.get('prj_desc')
    print('DATA:', prj_link, prj_desc, prj_name)

    if prj_link and prj_desc and prj_name:
      Experience.objects.create(prj_name=prj_name, prj_link=prj_link, prj_desc=prj_desc)			 
      return redirect('skill')
    else:
      return render(request, "edu/add_experience.html",{'errors':"Invalid Data....please add valid data"})
  
  return render(request, "edu/add_experience.html")


@login_required(login_url='login')
def add_work_experience(request):
  if request.method == "POST":
    position = request.POST.get('position')
    company_name = request.POST.get('company_name')
    desc = request.POST.get('desc')
    technologies = request.POST.get('technologies')
    work_duration = request.POST.get('work_duration')
    print('DATA:', company_name, work_duration, position)

    if company_name and work_duration and position and desc and technologies:
      Work_Experience.objects.create(position=position,company_name=company_name,work_duration=work_duration,desc=desc,technologies=technologies)			 
      return redirect('skill')
    else:
      return render(
        request, "edu/add_work_experience.html",
        {'errors': "Invalid Data....please add valid data"})
  
  return render(request, "edu/add_work_experience.html")


@login_required(login_url='login')
def update_resume(request):
   if request.method == 'POST' and request.FILES['resume']:
    pdf_file = request.FILES['resume']
    fs = FileSystemStorage()
    # Remove the old resume if it exists
    # old_data = Resume.objects.last()
    # if old_data:
    #     old_file_path = old_data.resume_data.path
    #     if os.path.exists(old_file_path):
    #         os.remove(old_file_path)
    filename = fs.save('resume_data/' + pdf_file.name, pdf_file)
    uploaded_file_url = fs.url(filename)
    document = Resume(resume_data=uploaded_file_url)
    document.save()
    return redirect('skill')
   return render(request, "edu/update_resume.html")


def download_resume(request):
    uploaded_file = Resume.objects.last()
    if uploaded_file and uploaded_file.resume_data:
        try:
            # Get the relative file path from the URL (resume_data is a URL)
            file_name = uploaded_file.resume_data.name  # e.g., 'resume_data/Resume__Bdh2BuG.pdf'
            print(f"Relative file name: {file_name}")

            # Remove any leading '/media/' if it exists
            if file_name.startswith('/media/'):
                file_name = file_name[7:]

            # Construct the full file path by joining MEDIA_ROOT with the corrected file name
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            print(f"Generated file path: {file_path}")
            
            # Check if the file path is within the MEDIA_ROOT folder
            if not file_path.startswith(settings.MEDIA_ROOT):
                raise SuspiciousFileOperation("The file is located outside of the media directory.")
            
            # Ensure the file exists
            if not os.path.exists(file_path):
                print(f"File does not exist: {file_path}")
                return HttpResponse("File not found", status=404)
            
            # Open the file and send it as a response
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{uploaded_file.resume_data.name}"'
                return response
        
        except FileNotFoundError:
            print("File not found.")
            return HttpResponse("File not found", status=404)
        except SuspiciousFileOperation as e:
            print(f"Suspicious file operation: {str(e)}")
            return HttpResponse(str(e), status=400)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return HttpResponse(f"Unexpected error: {str(e)}", status=500)
    
    return HttpResponse("No resume found", status=404)


def view_resume(request):
  try:
    resume = Resume.objects.last()
    if not resume or not resume.resume_data:
       raise Http404('No resume found')
    
    file_name = resume.resume_data.name  
    if file_name.startswith('/media/'):
        file_name = file_name[7:]
    # Construct the full file path by joining MEDIA_ROOT with the corrected file name
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    if not file_path.startswith(settings.MEDIA_ROOT):
        raise SuspiciousFileOperation("The file is located outside of the media directory.")
            
    # Ensure the file exists
    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
        return HttpResponse("File not found", status=404)
    
    # Open the file and send it as a response
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.resume_data.name}"'
        return response
  except:
    return Http404()

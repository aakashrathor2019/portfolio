from django.shortcuts import render,redirect
from core.models import Skill,Certifications,Experience,Work_Experience

# Create your views here.
def  skill(request):
	skill_data=Skill.objects.all()
	cert_data=Certifications.objects.all()
	exp_data= Experience.objects.all()
	work_exp_data=Work_Experience.objects.all().order_by('-id')
	context={
			'skill':'active',
			'skill_data':skill_data,
			'cert_data':cert_data,
			'exp_data':exp_data,
			'work_exp_data':work_exp_data,
			}
	print(skill_data)
	return render(request,'edu/skill.html',context )


def update_skills(request):
	if request.method == "POST":
		name=request.POST.get('name')
		desc= request.POST.get('desc')
		print('inide update skills function')
		existing_data=Skill.objects.filter(name=name).first()
		print('value of data:',existing_data)
		if name and desc:
			if not existing_data:
				print('Name and Proficiency:',name,desc)
				data= Skill.objects.create(name=name,desc=desc)
				return redirect('skill')
			else:
				print('inside else',existing_data)
				existing_data.name=name
				existing_data.desc=desc
				existing_data.save()
				return redirect('skill')
		else:
			return render(request,"edu/update_skills.html",{'error':'Please enter valid data...'})
		
	return  render(request,"edu/update_skills.html")


def add_certifications(request):
	if request.method=="POST":
		cert_name=request.POST.get('cert_name')
		cert_duration=request.POST.get('cert_duration')
		cert_from=request.POST.get('cert_from')
		print('DATA:',cert_duration,cert_from,cert_name)

		if cert_duration and cert_from and cert_name:
			Certifications.objects.create(cert_name=cert_name,cert_duration=cert_duration,cert_from=cert_from)
			return redirect(skill)
		else:
			return render(request,"edu/add_certifications.html",{'errors':"Invalid Data....please add valid data"})
	
	return render(request,"edu/add_certifications.html")


def add_experience(request):
	if request.method=="POST":
		prj_name=request.POST.get('prj_name')
		prj_link=request.POST.get('prj_link')
		prj_desc=request.POST.get('prj_desc')
		print('DATA:',prj_link,prj_desc,prj_name)

		if prj_link and prj_desc and prj_name:
			Experience.objects.create(prj_name=prj_name,prj_link=prj_link,prj_desc=prj_desc)			 
			return redirect(skill)
		else:
			return render(request,"edu/add_experience.html",{'errors':"Invalid Data....please add valid data"})
	
	return render(request,"edu/add_experience.html")

def add_work_experience(request):
	if request.method=="POST":
		position=request.POST.get('position')
		company_name=request.POST.get('company_name')
		desc=request.POST.get('desc')
		technologies=request.POST.get('technologies')
		work_duration=request.POST.get('work_duration')
		print('DATA:',company_name,work_duration,position)

		if company_name and work_duration and position and desc and technologies:
			Work_Experience.objects.create(position=position,company_name=company_name,work_duration=work_duration,desc=desc,technologies=technologies)			 
			return redirect(skill)
		else:
			return render(request,"edu/add_work_experience.html",{'errors':"Invalid Data....please add valid data"})
	
	return render(request,"edu/add_work_experience.html")
		

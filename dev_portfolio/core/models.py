from django.db import models


# Create your models here.
class Contact(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField()
  subject=models.CharField(max_length=100)
  message=models.TextField()

  def __str__(self):
    return f"{self.name}"


class Skill(models.Model):
  name=models.CharField(max_length=50)
  desc= models.TextField(null=True)

  def __str__(self):
    return f"{self.name}"


class Experience(models.Model):
  prj_name = models.CharField(max_length=100)
  prj_link = models.URLField(max_length=200,unique=True,blank=True)
  prj_desc=models.TextField()

  def __str__(self):
    return f"{self.prj_name}"


class Certifications(models.Model):
  cert_name=models.CharField(max_length=100)
  cert_duration=models.CharField(max_length=50) 
  cert_from=models.CharField(max_length=100)

  def __str__(self):
    return f"{self.cert_name}"


class Work_Experience(models.Model):
  position=models.CharField(max_length=50)
  company_name=models.CharField(max_length=50)
  work_duration=models.CharField(max_length=50)
  desc=models.TextField()
  technologies=models.TextField()

  def __str__(self):
    return f"{self.position}"


class Resume(models.Model):
  resume_data = models.FileField(upload_to='resume_data/')

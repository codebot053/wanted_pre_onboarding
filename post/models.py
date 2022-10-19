from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(db_index=True, max_length=100)
    nation = models.CharField(db_index=True, max_length=100)
    location = models.CharField(db_index=True,max_length=100)
     
    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name="회사명" ,on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    job_reward = models.IntegerField("채용보상금")
    content = models.TextField("채용내용",max_length=500)
    technologies_needed = models.ManyToManyField(to="Technology", verbose_name="사용기술")

    def __str__(self):
        return self.content
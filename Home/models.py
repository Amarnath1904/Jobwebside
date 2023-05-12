from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class users(User):

    
    ProfilePhoto = models.ImageField(upload_to='ProfilePhoto', null=True, default="ProfilePhoto/default.png")
    Resume = models.FileField(upload_to='Resume', null=True, default="Resume/default.pdf")
    Country = models.CharField(max_length=100, null=True)
    Street_address = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True)
    Zip = models.CharField(max_length=100, null=True)
    About = models.CharField(max_length=1000, null=True)



class Jobs(models.Model):
    Id = models.AutoField(primary_key=True)
    JobTitle = models.CharField(max_length=100)
    JobDescription = models.CharField(max_length=1000)
    JobLocation = models.CharField(max_length=100)
    JobType = models.CharField(max_length=100)
    JobCategory = models.CharField(max_length=100)
    JobSalary = models.CharField(max_length=100)
    JObDate = models.DateField(auto_now_add=True)
    JobCompany = models.CharField(max_length=100)
    SubmitedByResumas = models.ManyToManyField(users, related_name='SubmitedByResumas', blank=True)


    def __str__(self) -> str:
        return self.JobTitle




User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True
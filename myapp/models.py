from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return 'Enquiry from ' + self.fname + ' ' + self.lname

class Course(models.Model):
    sno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=255)
    csummary = models.TextField()
    cimg = models.ImageField(upload_to='courseimages')
    heading = models.CharField(max_length=100)
    slug = models.SlugField(max_length=500)
    
    
    def __str__(self):
        return self.cname
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    course = models.CharField(max_length=50)

    def __str__(self):
        return 'Enquiry from ' + self.name + ' ' + self.course
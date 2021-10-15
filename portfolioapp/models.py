from django.db import models

# Create your models here.

class About(models.Model):
    name=models.CharField(max_length=60)
    career=models.CharField(max_length=50, default='web developer')
    email=models.EmailField()
    phone=models.CharField(max_length=11,null=True)
    adress=models.CharField(max_length=50,null=True)
    profile_pic=models.ImageField(upload_to='images')
    bio=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Tag,on_delete=models.SET_NULL ,null=True,default='fornt')

    class Meta:
        verbose_name='skill'
        verbose_name_plural='skills'


    def __str__(self):
        return self.name                    


class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    link_github=models.URLField()
    link_live=models.URLField(null=True,blank=True)
    picture_pro=models.ImageField(upload_to='projects',default='projects/django.png')        


    def __str__(self):
        return self.name
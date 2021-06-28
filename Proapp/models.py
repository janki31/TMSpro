from django.db import models

# Create your models here.

class Image_gallery(models.Model):
    image_id=models.AutoField(primary_key=True)
    image_name=models.CharField(max_length=50)
    category=models.CharField(max_length=100,default="")
    image_desc=models.TextField(default="")
    image_file=models.ImageField(upload_to="proapp/images",default="")

    def __str__(self):
        return self.image_name

class Contact_detail(models.Model):
    con_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100,default="")
    phone_no=models.IntegerField(default=0)
    message=models.TextField(default="")

    def __str__(self):
        return self.name

class Pooja_booking(models.Model):
    pid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    address=models.TextField(default="")
    emailid=models.EmailField(max_length=50,default="")
    nopeople=models.IntegerField(default=0)
    pdate=models.DateField()
    ptime=models.TimeField()
    pcategory=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default="")
    zipcode=models.IntegerField(default=0)

    def __str__(self):
        return self.fname

class Fund_donation(models.Model):
    fid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    address=models.TextField(default="")
    emailid=models.EmailField(max_length=50,default="")
    mobileno=models.IntegerField(default=0)
    city=models.CharField(max_length=50,default="")
    zipcode=models.IntegerField(default=0)
    damount=models.IntegerField(default=0)

    def __str__(self):
        return self.fname

class Blood_donation(models.Model):
    bid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    address=models.TextField(default="")
    emailid=models.EmailField(max_length=50,default="")
    mobileno=models.IntegerField(default=0)
    bdate = models.DateField()
    btime = models.TimeField()
    bgroup=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default="")
    zipcode=models.IntegerField(default=0)
    feedback=models.TextField()

    def __str__(self):
        return self.fname



from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)


class University(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)
        verbose_name = "Universitie"

class State(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)

class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)


class District(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)

class College(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University)
    address = models.TextField()
    state= models.ForeignKey(State)
    city = models.ForeignKey(City)
    district = models.ForeignKey(District)
    pincode = models.PositiveIntegerField()
    phone = models.CharField(max_length=30)
    fax = models.PositiveIntegerField(default=0, blank=True)
    email = models.EmailField()
    website = models.URLField(max_length=50, default=None, blank=True)
    director = models.CharField(max_length=200, default=None, blank=True)
    principal = models.CharField(max_length=200, default=None, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "College"

class CollegeCourse(models.Model):
    college = models.ForeignKey(College)
    department_name = models.ForeignKey(Course)
    hod_name = models.CharField(max_length=200, blank=True)
    hod_email = models.CharField(max_length=200, blank=True)
    hod_phone = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.department_name
    
    class Meta:
        verbose_name = "Department"

from django.db import models

# Create your models here.
class Year(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)


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
 
class District(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)

class InstituteType(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (("name"),)

class College(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University)
    institute_type = models.ForeignKey(InstituteType)
    year_of_establish = models.ForeignKey(Year)
    address = models.TextField()
    district = models.ForeignKey(District)
    pincode = models.PositiveIntegerField()
    phone = models.CharField(max_length=30)
    fax = models.PositiveIntegerField(default=0, blank=True)
    email = models.EmailField()
    website = models.URLField(max_length=50)
    railway_station = models.CharField(max_length=200, blank=True)
    bus_stand = models.CharField(max_length=200, blank=True)
    director_principal = models.CharField(max_length=200)
    hostel_intake_boys = models.PositiveIntegerField(default=0)
    hostel_intake_girls = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "College"

class CollegeCourse(models.Model):
    college = models.ForeignKey(College)
    course_name = models.ForeignKey(Course)
    accredation = models.CharField(max_length=50, blank=True, default=None)
    course_state_year = models.ForeignKey(Year)
    general_intake = models.CharField(max_length=100, blank=True, default=None)
    general_choicecode = models.CharField(max_length=100, blank=True, default=None)
    tfes_intake = models.CharField(max_length=100, blank=True, default=None)
    tfes_choicecode = models.CharField(max_length=100, blank=True, default=None)
    high_court_intake = models.CharField(max_length=100, blank=True, default=None)
    high_court_choicecode = models.CharField(max_length=100, blank=True, default=None)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.course_name
    
    class Meta:
        verbose_name = "College Courses"

from django.db import models
from makeReports.choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from gdstorage.storage import GoogleDriveStorage
from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe
import os
gd_storage = GoogleDriveStorage()
class NonArchivedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)
class Report(models.Model):
    year = models.PositiveIntegerField()
    author = models.CharField(max_length=100, blank=True)
    degreeProgram = models.ForeignKey('DegreeProgram', on_delete=models.CASCADE)
    date_range_of_reported_data = models.CharField(max_length=500,blank=True, null=True)
    rubric = models.OneToOneField('GradedRubric', on_delete=models.SET_NULL, null=True)
    section1Comment = models.CharField(max_length=2000, blank=True, null=True)
    section2Comment = models.CharField(max_length=2000, blank=True, null=True)
    section3Comment = models.CharField(max_length=2000, blank=True, null=True)
    section4Comment = models.CharField(max_length=2000, blank=True, null=True)
    submitted = models.BooleanField()
    returned = models.BooleanField(default=False)
    numberOfSLOs = models.PositiveIntegerField(default=0)
class College(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active_objects = NonArchivedManager()
    def __str__(self):
        return self.name
class Department(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active_objects = NonArchivedManager()    
    def __str__(self):
        return self.name
class DegreeProgram(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=75, choices= LEVELS)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cycle = models.IntegerField(blank=True, null=True)
    startingYear = models.PositiveIntegerField(blank=True, null=True)
    #not all degree programs are on a clear cycle
    active = models.BooleanField(default=True)
    objects = models.Manager()
    active_objects = NonArchivedManager()
    def __str__(self):
        return self.name
class SLO(models.Model):
    blooms = models.CharField(choices=BLOOMS_CHOICES,max_length=50)
    gradGoals = models.ManyToManyField('GradGoal')
    numberOfUses = models.PositiveIntegerField(default=1)
class SLOInReport(models.Model):
    date = models.DateField()
    goalText = models.CharField(max_length=600)
    slo = models.ForeignKey(SLO, on_delete=models.CASCADE)    
    changedFromPrior = models.BooleanField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)
    numberOfAssess = models.PositiveIntegerField(default=0)
    def __str__(self):
        return mark_safe(self.goalText)
class GradGoal(models.Model):
    text = models.CharField(max_length=300)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    active_objects = NonArchivedManager()
    def __str__(self):
        return mark_safe(self.text)
class SLOsToStakeholder(models.Model):
    text = models.CharField(max_length=2000)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return mark_safe(self.text)
class Assessment(models.Model):
    title = models.CharField(max_length=300)
    domainExamination = models.BooleanField()
    domainProduct = models.BooleanField()
    domainPerformance = models.BooleanField()
    directMeasure = models.BooleanField()
    numberOfUses = models.PositiveIntegerField(default=1)
    #false = indirect measure
    def __str__(self):
        return self.title
class AssessmentVersion(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    slo = models.ForeignKey(SLOInReport, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    changedFromPrior = models.BooleanField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    finalTerm = models.BooleanField()
    #false = final year
    where = models.CharField(max_length=200)
    allStudents = models.BooleanField()
    #false = sample of students
    sampleDescription = models.CharField(max_length=200,blank=True,null=True)
    frequencyChoice = models.CharField(max_length=100,choices=FREQUENCY_CHOICES,default="O")
    frequency = models.CharField(max_length=100)
    #the below are percentage points
    threshold = models.CharField(max_length=500) # Should be text field, change later
    target = models.PositiveIntegerField()
    supplements = models.ManyToManyField('AssessmentSupplement')
    def __str__(self):
        return self.assessment.title
class AssessmentSupplement(models.Model):
    supplement = models.FileField(upload_to='asssements/supplements', storage=gd_storage, validators=[FileExtensionValidator(allowed_extensions=('pdf',))])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return os.path.basename(self.supplement.name)
class Subassessment(models.Model):
    assessmentVersion = models.ForeignKey(AssessmentVersion, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    proficient = models.PositiveIntegerField()
class AssessmentData(models.Model):
    assessmentVersion = models.ForeignKey(AssessmentVersion,on_delete=models.CASCADE)
    dataRange = models.CharField(max_length=500)
    numberStudents = models.PositiveIntegerField()
    overallProficient = models.PositiveIntegerField(blank=True)
class AssessmentAggregate(models.Model):
    assessmentVersion = models.ForeignKey(AssessmentVersion, on_delete=models.CASCADE)
    aggregate_proficiency = models.PositiveIntegerField(verbose_name="aggregate proficiency percentage")
    met = models.BooleanField()
    def __str__(self):
        return str(self.aggregate_proficiency)
class DataAdditionalInformation(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    comment = models.CharField(max_length=3000, blank=True, default="")
    supplement = models.FileField(upload_to='data/supplements', storage=gd_storage, validators=[FileExtensionValidator(allowed_extensions=('pdf',))])
    def __str__(self):
        return os.path.basename(self.supplement.name)
class SLOStatus(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=SLO_STATUS_CHOICES)
    SLO = models.ForeignKey(SLO, on_delete=models.CASCADE)
class ResultCommunicate(models.Model):
    text = models.CharField(max_length=3000)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
class DecisionsActions(models.Model):
    SLO = models.ForeignKey(SLO, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    text = models.CharField(max_length=3000, blank=True, default="")
    decisionProcess = models.CharField(max_length=3000, blank=True, default="")
    decisionMakers = models.CharField(max_length=3000, blank=True, default="")
    decisionTimeline = models.CharField(max_length=3000, blank=True, default="")
    dataUsed = models.CharField(max_length=3000, blank=True, default="")
    actionTimeline = models.CharField(max_length=3000, blank=True, default="")
class Rubric(models.Model):
    date = models.DateField()
    fullFile = models.FileField(default='settings.STATIC_ROOT/norubric.pdf',verbose_name="rubric file",upload_to='rubrics', storage=gd_storage, null=True,blank=True, validators=[FileExtensionValidator(allowed_extensions=('pdf',))])
    name = models.CharField(max_length = 150, default="Rubric")
    def __str__(self):
        return self.name
class GradedRubric(models.Model):
    rubricVersion = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    section1Comment = models.CharField(max_length=2000,blank=True,null=True)
    section2Comment = models.CharField(max_length=2000,blank=True,null=True)
    section3Comment = models.CharField(max_length=2000,blank=True,null=True)
    section4Comment = models.CharField(max_length=2000,blank=True,null=True)
    generalComment = models.CharField(max_length=2000,blank=True,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.rubricVersion.name
class RubricItem(models.Model):
    text = models.CharField(max_length=1000)
    section = models.PositiveIntegerField(choices=SECTIONS)
    rubricVersion = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    abbreviation = models.CharField(max_length=20, default="", blank=True)
    DMEtext = models.CharField(max_length=1000, default="", blank=True)
    MEtext = models.CharField(max_length=1000, default="", blank=True)
    EEtext = models.CharField(max_length=1000, default="", blank=True)
    def __str__(self):
        return mark_safe(self.text)
class GradedRubricItem(models.Model):
    rubric = models.ForeignKey('GradedRubric', on_delete=models.CASCADE)
    item = models.ForeignKey(RubricItem, on_delete=models.CASCADE)
    grade = models.CharField(max_length=300, choices=RUBRIC_GRADES_CHOICES)
class ReportSupplement(models.Model):
    supplement = models.FileField(upload_to='data/supplements', storage=gd_storage,validators=[FileExtensionValidator(allowed_extensions=('pdf',))])
    report = models.ForeignKey('Report', on_delete=models.CASCADE)
    def __str__(self):
        return os.path.basename(self.supplement.name)
class Announcement(models.Model):
    text = models.CharField(max_length=2000,blank=True)
    expiration = models.DateField()
    creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return mark_safe(self.text)
class Profile(models.Model):
    #first name, last name and email are included in the built-in User class. Access them through the user field
    aac = models.BooleanField(null=True)
    #False = faculty member/dept account
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
@receiver(post_save,sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    #this updates profile when user is updated
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget
class CreateNewAssessment(forms.Form):
    slo = forms.ModelChoiceField(label="SLO",queryset=None)
    title = forms.CharField(max_length=300)
    domain = forms.MultipleChoiceField(choices = (("Pe", "Performance"), ("Pr","Product"), ("Ex","Examination") ), widget=forms.CheckboxSelectMultiple,required=False)
    directMeasure = forms.ChoiceField(label="Direct measure",choices = ((True, "Direct Measure"), (False,"Indirect Measure")))
    description = forms.CharField(widget=SummernoteWidget(), max_length=1000)
    finalTerm = forms.ChoiceField(label="When assessment takes place",choices = ((True, "In final term"), (False, "In final year")))
    where = forms.CharField(label="Where does assessment take place",widget= SummernoteWidget(),max_length=200)
    allStudents = forms.ChoiceField(label="Are all students assessed?",choices = ((True, "All Students"), (False,"Sample of Students")))
    sampleDescription = forms.CharField(label="What students are sampled",widget= SummernoteWidget(), max_length=200, required=False)
    frequency = forms.CharField(widget=SummernoteWidget(), max_length=100)
    threshold = forms.CharField(max_length=500,label="Proficiency Threshold")
    target = forms.IntegerField(min_value=0, label="Program Proficiency Target: % of students that achieve the proficiency threshold")
    
    def __init__(self,*args,**kwargs):
        sloQS = kwargs.pop('sloQS',None)
        super(CreateNewAssessment,self).__init__(*args,**kwargs)
        self.fields['slo'].queryset = sloQS

class ImportAssessmentForm(forms.Form):
    assessment = forms.ModelMultipleChoiceField(queryset=None)
    slo = forms.ModelChoiceField(label="SLO",queryset=None)
    def __init__(self, *args, **kwargs):
        assessChoices = kwargs.pop('assessChoices',None)
        sloChoices = kwargs.pop('slos',None)
        super(ImportAssessmentForm, self).__init__(*args, **kwargs)
        self.fields['assessment'].queryset = assessChoices
        self.fields['slo'].queryset = sloChoices

class EditNewAssessmentForm(forms.Form):
    slo = forms.ModelChoiceField(label="SLO",queryset=None)
    title = forms.CharField(max_length=300)
    domain = forms.MultipleChoiceField(choices = (("Pe", "Performance"), ("Pr","Product"), ("Ex","Examination") ), widget=forms.CheckboxSelectMultiple)
    directMeasure = forms.ChoiceField(label="Direct Measure?",choices = ((True, "Direct Measure"), (False,"Indirect Measure")))
    description = forms.CharField(widget=SummernoteWidget(), max_length=1000)
    finalTerm = forms.ChoiceField(label="Does it occur in the final term?",choices = ((True, "In final term"), (False, "In final year")))
    where = forms.CharField(label="Where is the assessment administered?",widget= SummernoteWidget(), max_length=200)
    allStudents = forms.ChoiceField(label="Are all students assessed?",choices = ((True, "All Students"), (False,"Sample of Students")))
    sampleDescription = forms.CharField(label="Describe students sampled",widget= SummernoteWidget(), max_length=200)
    frequency = forms.CharField(widget=SummernoteWidget(), max_length=100)
    threshold = forms.CharField(max_length=500,label="Proficiency Threshold")
    target = forms.IntegerField(min_value=0, label="Program Proficiency Target: % of students that achieve the proficiency threshold")
    def __init__(self,*args,**kwargs):
        sloQS = kwargs.pop('sloQS',None)
        super(EditNewAssessmentForm,self).__init__(*args,**kwargs)
        self.fields['slo'].queryset = sloQS

class EditImportedAssessmentForm(forms.Form):
    slo = forms.ModelChoiceField(queryset=None,label="SLO")
    description = forms.CharField(widget=SummernoteWidget(), max_length=1000, label="Description: ")
    finalTerm = forms.ChoiceField(label="Does the assessment occur during the final term?",choices = ((True, "In final term"), (False, "In final year")))
    where = forms.CharField(label="Where are students assessed?",widget= SummernoteWidget(), max_length=200)
    allStudents = forms.ChoiceField(label="Are all students assessed?",choices = ((True, "All Students"), (False,"Sample of Students")))
    sampleDescription = forms.CharField(label="Describe the sample of students assessed",widget= SummernoteWidget(), max_length=200)
    frequency = forms.CharField(widget=SummernoteWidget(), max_length=100)
    threshold = forms.CharField(max_length=500,label="Proficiency Threshold")
    target = forms.IntegerField(min_value=0, label="Program Proficiency Target: % of students that achieve the proficiency threshold")
    def __init__(self,*args,**kwargs):
        sloQS = kwargs.pop('sloQS',None)
        super(EditImportedAssessmentForm,self).__init__(*args,**kwargs)
        self.fields['slo'].queryset = sloQS


class ImportSupplementsForm(forms.Form):
    sup = forms.ModelChoiceField(queryset=None, label="Supplement Upload")
    def __init__(self, *args, **kwargs):
        supChoices = kwargs.pop('supChoices',None)
        super(ImportSupplementsForm, self).__init__(*args, **kwargs)
        self.fields['sup'].queryset = supChoices
from django import forms
from makeReports.models import *
from makeReports.choices import *
from django_summernote.widgets import SummernoteWidget
from .cleaners import CleanSummer
from django.core.exceptions import ValidationError
"""
Forms relating to inputting SLOs
"""
class CreateNewSLO(CleanSummer,forms.Form):
    """
    Form to create a new SLO
    """
    text = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control col-7'}), label="SLO: ") 
    blooms = forms.ChoiceField(choices=BLOOMS_CHOICES, label="Highest Bloom's Taxonomy Level: ", widget=forms.Select(attrs={'class':'form-control col-5'}))
    gradGoals = forms.ModelMultipleChoiceField(queryset=GradGoal.active_objects.all(), required=False,widget=forms.CheckboxSelectMultiple, label="Graduate-level Goals: ")
    summer_max_length = 1000
    def __init__(self,*args,**kwargs):
        """
        Initializes form and deletes grad field if undergraduate level
        
        Keyword Args:
            grad (Boolean): whether it is a graduate level program
        """
        grad = kwargs.pop('grad',None)
        super(CreateNewSLO,self).__init__(*args,**kwargs)
        if not grad:
            del self.fields['gradGoals']
class ImportSLOForm(forms.Form):
    """
    Form to import pre-existing SLO
    """
    slo = forms.ModelMultipleChoiceField(queryset=None, label="SLOs to Import: ", widget=forms.Select(attrs={'class':'form-control col-5'}))
    importAssessments = forms.BooleanField(required=False,label="Also import assessments?")
    #of type SLOInReport
    def __init__(self, *args, **kwargs):
        """
        Initializes form, including setting SLO choices

        Keyword Args:
            sloChoices (QuerySet): SLO choices
        """
        sloChoices = kwargs.pop('sloChoices',None)
        super(ImportSLOForm, self).__init__(*args, **kwargs)
        self.fields['slo'].queryset = sloChoices
class EditNewSLOForm(CleanSummer,forms.Form):
    """
    Form to edit a new SLO (no restrictions)
    """
    text = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control col-7'}), label="SLO: ")
    blooms = forms.ChoiceField(choices=BLOOMS_CHOICES, required=False, label="Highest Bloom's Taxonomy Level: ",widget=forms.Select(attrs={'class':'form-control col-5'}))
    gradGoals = forms.ModelMultipleChoiceField(queryset=GradGoal.active_objects.all(), required=False,widget=forms.CheckboxSelectMultiple(), label="Graduate-level Goals: ")
    
    summer_max_length = 1000
    def __init__(self,*args,**kwargs):
        """
        Initializes form and deletes grad if undergraduate program

        Keyword Args;
            grad (Boolean): whether graduate level program
        """
        grad = kwargs.pop('grad',None)
        super(EditNewSLOForm,self).__init__(*args,**kwargs)
        if not grad:
            del self.fields['gradGoals']
class EditImportedSLOForm(CleanSummer,forms.Form):
    """
    Form to edit imported SLO (more restricted than new)
    """
    text = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control col-7'}), label="SLO: ", max_length=1000)
    summer_max_length = 1000
class Single2000Textbox(CleanSummer,forms.Form):
    """
    Form for a single 2000 character textbox
    """
    text = forms.CharField(widget=SummernoteWidget(attrs={'style':'width:750px'}),label="")
    summer_max_length = 2000

class ImportStakeholderForm(forms.Form):
    """
    Form to import pre-existing stakeholder communication text
    """
    stk = forms.ModelChoiceField(queryset=None, label="Stakeholder Communication Methods", widget=forms.Select(attrs={'class':'form-control col-7'}))
    def __init__(self, *args, **kwargs):
        """
        Initializes form, including setting choices for stakeholder communication

        Keyword Args:
            stkChoice (QuerySet): stakeholder communication text choices
        """
        stkChoices = kwargs.pop('stkChoices',None)
        super(ImportStakeholderForm, self).__init__(*args, **kwargs)
        self.fields['stk'].queryset = stkChoices

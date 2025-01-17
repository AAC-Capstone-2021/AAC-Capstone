"""
Forms relating to inputting and modifying SLOs
"""
from django import forms
from django.template.defaultfilters import register
from django_summernote.widgets import SummernoteWidget
from makeReports.models import GradGoal
from makeReports.choices import BLOOMS_CHOICES
from makeReports.choices import ACCREDITING_BODY_MEASURES
from makeReports.choices import ACCREDITING_BODY_DOMAIN
from makeReports.models import AccreditingBody
from .cleaners import CleanSummer
from .widgets import SLOMultipleChoicesJSWidget, StkChoicesJSWidget

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]

class CreateNewSLO(forms.Form):
    """
    Form to create a new SLO
    """
    text = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control col-7'}), label=False, max_length=1000) 
    blooms = forms.ChoiceField(choices=BLOOMS_CHOICES, label="Highest Bloom's Taxonomy Level: ", widget=forms.Select(attrs={'class':'form-control col-5'}))
    gradGoals = forms.ModelMultipleChoiceField(widget= forms.CheckboxSelectMultiple, queryset=GradGoal.active_objects.all(), required=False, label="Graduate-level Goals")
    accreditingBody = forms.BooleanField(label='Accrediting_body', required=False)
    imported = forms.BooleanField(required=False)
    importedFrom = forms.CharField(max_length = 50, disabled = True, required=False)

    def __init__(self,*args,**kwargs):
        """
        Initializes form and deletes grad field if undergraduate level
        
        Keyword Args:
            grad (bool): whether it is a graduate level program
        """
        grad = kwargs.pop('grad',None)
        super(CreateNewSLO,self).__init__(*args,**kwargs)
        if not grad:
            del self.fields['gradGoals']

class ImportSLOForm(forms.Form):
    """
    Form to import pre-existing SLO
    """
    slo = forms.ModelMultipleChoiceField(queryset=None, label="SLOs to Import: ", widget=SLOMultipleChoicesJSWidget(attrs={'class':'form-control col-9'}))
    importAssessments = forms.BooleanField(required=False,label="Also import assessments with SLO")
    def __init__(self, *args, **kwargs):
        """
        Initializes form, including setting SLO choices

        Keyword Args:
            sloChoices (QuerySet): SLO choices (of type :class:`~makeReports.models.basic_models.SLOInReport`)
        """
        sloChoices = kwargs.pop('sloChoices',None)
        super(ImportSLOForm, self).__init__(*args, **kwargs)
        self.fields['slo'].queryset = sloChoices
    def clean(self):
        return super(ImportSLOForm,self).clean()
        
class EditImportedSLOForm(CleanSummer,forms.Form):
    """
    Form to edit imported SLO (more restricted than new)
    """
    text = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control col-7'}), label=False, max_length=1000)
    accreditingBody = forms.BooleanField(label='Accrediting_body')
    summer_max_length = 1000
class Single2000Textbox(CleanSummer,forms.Form):
    """
    Form for a single 2000 character textbox
    """
    internal_stakeholders = forms.MultipleChoiceField(required = False, choices = (("Fa", "Faculty"), ("St", "Students"), ("Oi", "Other Internal Stakeholder") ), widget=forms.CheckboxSelectMultiple)
    external_stakeholders = forms.MultipleChoiceField(required = False, choices = (("Ps", "Prospective Students"), ("Al", "Alumni"), ("Em", "Employers"),("Cm", "Community Members/Groups") ,("Oe", "Other External Stakeholder") ), widget=forms.CheckboxSelectMultiple)
    text = forms.CharField(widget=SummernoteWidget(attrs={'style':'width:750px'}),label="")
    summer_max_length = 2000

class ImportStakeholderForm(forms.Form):
    """
    Form to import pre-existing stakeholder communication text
    """
    stk = forms.ModelChoiceField(queryset=None, label="Stakeholder Communication Methods", widget=StkChoicesJSWidget(attrs={'class':'form-control col-7'}))
    def __init__(self, *args, **kwargs):
        """
        Initializes form, including setting choices for stakeholder communication

        Keyword Args:
            stkChoice (QuerySet): stakeholder communication text choices
        """
        stkChoices = kwargs.pop('stkChoices',None)
        super(ImportStakeholderForm, self).__init__(*args, **kwargs)
        self.fields['stk'].queryset = stkChoices

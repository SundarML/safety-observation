# observations/forms.py
from django import forms
from .models import Observation

class ObservationCreateForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['title','location','description','severity','photo_before','assigned_to','target_date']

class RectificationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['rectification_details','photo_after','target_date']

class VerificationForm(forms.ModelForm):
    APPROVAL_CHOICES = [
        ('approve', 'Approve and Close'),
        ('reject', 'Reject (Send Back to Action Owner)'),
    ]

    verification_action = forms.ChoiceField(
        choices=APPROVAL_CHOICES,
        widget=forms.RadioSelect,
        label="Verification Decision"
    )
    class Meta:
        model = Observation
        fields = ['verification_comment']
        widgets = {
            'verification_comment': forms.Textarea(attrs={'rows': 3}),
        }
    # approved = forms.BooleanField(required=False)
    # comment = forms.CharField(widget=forms.Textarea, required=False)

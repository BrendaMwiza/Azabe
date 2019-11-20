from django import forms
from .models import Post, Child, Partners,Activities,Parents
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
class RegChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = []
# class RegTrainerForm(forms.ModelForm):
#     class Meta:
#         model = Trainer
#         exclude = []

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activities
        exclude = []
class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Parents
        exclude = ['email']

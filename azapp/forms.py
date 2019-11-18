from django import forms
from .models import Post, Child, Partners
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

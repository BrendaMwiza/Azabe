from django import forms
from .models import Post, Child, Partners, Parents
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
class RegChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = []
class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Parents
        exclude = ['email']

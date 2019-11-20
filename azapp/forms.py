from django import forms
from .models import Post, Child, Partners,Parents
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
class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Parents
        exclude = ['email']
class UpdateParForm(forms.ModelForm):
    class Meta:
        model = Partners
        exclude = ['email']
class partnerForm(forms.ModelForm):
    class Meta:
        model = Partners
        # exclude = ['approved']
        fields=('partner_name','description','partner_image')

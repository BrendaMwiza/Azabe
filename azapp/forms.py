from django import forms
from .models import Post, Child, Partners,Activities,Parents,Comments,Blog, CommentBlog
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
class RegChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ['parent']
# class RegTrainerForm(forms.ModelForm):
#     class Meta:
#         model = Trainer
#         exclude = []
class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Parents
        exclude = ['email','user']
class UpdateParForm(forms.ModelForm):
    class Meta:
        model = Partners
        exclude = ['email','user','approved']
class partnerForm(forms.ModelForm):
    class Meta:
        model = Partners
        # exclude = ['approved']
        fields=('partner_name','description','partner_image')
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activities
        exclude = []
class commentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['commented_by','commented_act']
class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['time','user']

class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        exclude = ['commenter','commented_blog']

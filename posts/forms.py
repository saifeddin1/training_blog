from django import forms
from .models import Post, Comment
from tinymce import TinyMCE





class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False



class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={
                'required': False, 'cols':30, 'rows':10
            }
            )
        )

    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
        widgets={
            'body' : forms.Textarea(attrs=
                {'style':'height:100px;width:100%;background-color:#f1f1f1;resize:none;border:none;margin-top:10px;'}),
        }   
        labels={
            'body' : 'Your Commment ',
        }
        # widget= {
        #     'name':forms.TextInput(attrs={
        #             'placeholder':'enter your name',
        # }),
        #     'email':forms.EmailInput(attrs={
        #             'placeholder':'enter your email',
        # }),
        # }
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    # body = forms.TextField(attrs={
    #                 'placeholder':'enter your name',
    #     })
    # email = forms.EmailArea(attrs={
    #             'placeholder':'enter your  email',
    # })
    class Meta:
        model = Comment
        fields = ['name','email', 'body']
        widget= {
            'name':forms.TextInput(attrs={
                    'placeholder':'enter your name',
        }),
            'email':forms.EmailInput(attrs={
                    'placeholder':'enter your email',
        }),
        }
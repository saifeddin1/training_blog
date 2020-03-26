from .models import Post
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content','created_at']
        widgets = {
            'created_at' : forms.DateInput(
                attrs={
                'type': 'date',
                'data-provide': 'datepicker',
                'data-date-format': 'yyyy-mm-dd',
            },
            format='%Y-%m-%d'
                    )

        }
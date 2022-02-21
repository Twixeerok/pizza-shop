from pyexpat import model
from django.forms import ModelForm, TextInput
from .models import  Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

        widgets = {
            'comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте комментарий'
            })
        }
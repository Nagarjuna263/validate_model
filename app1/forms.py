from django import forms
from app1.models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
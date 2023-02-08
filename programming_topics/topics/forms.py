from django.forms import ModelForm
from .models import Subtopic


class SubtopicForm(ModelForm):
    class Meta:
        model = Subtopic
        fields = '__all__'
from .models import Subject, Card
from django import forms


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name']


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['question', 'answer']


class CardUpdateForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['question', 'answer']
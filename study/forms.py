from django import forms
from cards.models import Subject


class SubjectSelectForm(forms.Form):

    name = forms.ModelChoiceField(queryset=Subject.objects.none().order_by('name'))

    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user', None)
        super(SubjectSelectForm,self).__init__(*args, **kwargs)
        self.fields['name'].queryset = Subject.objects.filter(user_id=user)





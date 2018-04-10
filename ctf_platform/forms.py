from django import forms


class FlagSubmissionForm(forms.Form):
    team = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Team name'}))
    flag = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Flag proposition'}))
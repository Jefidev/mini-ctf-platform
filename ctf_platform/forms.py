from django import forms


class FlagSubmissionForm(forms.Form):
    team = forms.CharField(max_length=100, label="Team name")
    pwd = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput)
    flag = forms.CharField(max_length=100, label="Flag proposition")
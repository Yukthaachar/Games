from django import forms
class InputForm(forms.Form):
    input = forms.IntegerField(label='Guess the number between 1 and 100')
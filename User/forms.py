from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=200, widget= forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter a todo role'}))


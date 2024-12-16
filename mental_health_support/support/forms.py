from django import forms

class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Your question', max_length=200)
    # Add more fields as necessary

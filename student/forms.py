from django import forms

class StudForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='Student Name')
    s_class=forms.CharField(max_length=30,label='Student Class')
    s_addr=forms.CharField(max_length=30,label='Student Address')
    s_school=forms.CharField(max_length=30,label='School Name')
    s_email=forms.EmailField(max_length=30,label='Student Email')
    
class SForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='Student Name')
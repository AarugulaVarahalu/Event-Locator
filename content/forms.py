from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()



class DateForm(forms.Form):
    search_date = forms.DateField(label='Enter Date', widget=forms.DateInput(attrs={'type': 'date'}))
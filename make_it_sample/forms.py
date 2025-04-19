from django import forms

class UploadFileForm(forms.Form):
    integer_input = forms.IntegerField(label="Number of languages to be included in the sample")
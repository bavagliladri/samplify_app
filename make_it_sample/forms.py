from django import forms


class UploadFileForm(forms.Form):
    csv_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label="Select CSV files")
    integer_input = forms.IntegerField(label="Number of languages to be included in the sample")
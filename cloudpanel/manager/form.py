from django import forms

class fileuploadform(forms.Form):
	file = forms.FileField()
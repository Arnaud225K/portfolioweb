from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={'class': 'form-control p-4','id':'name','autocomplete': 'off', 'placeholder':'Your name'}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.EmailInput(attrs={'class': 'form-control p-4','id':'email','autocomplete': 'off', 'placeholder':'Your email'}))
	subject = forms.CharField(max_length=255,
		widget=forms.TextInput(attrs={'class': 'form-control p-4','id':'subject','autocomplete': 'off', 'placeholder':'Subject'}))
	message = forms.CharField(max_length=1000, 
		widget=forms.Textarea(attrs={'class': 'form-control p-4','id':'message', 'placeholder':'Message'}))
	#reCAPTCHA token
	token = forms.CharField(
		widget=forms.HiddenInput())

	class Meta:
		model = Contact
		fields = ['name','email','subject','message']


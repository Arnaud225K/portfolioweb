from django.conf import settings
import requests
from django.http import JsonResponse




'''
Handles form error that are passed back to AJAX calls
'''
def FormErrors(*args):
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message




'''
Handles validation from reCAPTCHA
'''
def reCAPTCHAValidation(token):

	''' reCAPTCHA validation '''
	result = requests.post(
		'https://www.google.com/recaptcha/api/siteverify',
		 data={
		 	'secret': settings.RECAPTCHA_PRIVATE_KEY,
			'response': token
		 })

	return result.json()
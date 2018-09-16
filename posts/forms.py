from django import forms
from .models import Amice

class AmiceForms(forms.ModelForm):
	class Meta:
		model = Amice
		fields = ('first_name', 'last_name', 'lichting')

		labels = {
			"lichting": "lichting (jaartal)"
		}
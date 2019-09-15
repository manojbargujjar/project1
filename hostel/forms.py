from django import forms

from .models import *

class room_form(forms.ModelForm):
	
	class Meta:
		model = Room
		fields=['usr', 'hname','room_no','block','floor', 'bed_no','fees']

class complain_form(forms.ModelForm):

	class Meta:
		model = Complain
		fields = ['room_no','Complain','date']
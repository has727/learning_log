from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		# Removing the text in front of the text input box
		labels = {'text': 'New Topic'}
		# Tpoc_Choices = (
		# 	('A', 'A real A'),
		# 	('B', 'A real B'),
		# 	('C', 'A real C')
		# )
		# widgets ={'text': forms.Select(choices=Tpoc_Choices)}
		

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		# removing the text in front of the text input box
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80, 'rows': 20})}
		
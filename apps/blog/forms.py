from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
	'''
	博客表单
	'''
	class Meta:
		model = Blog
		fields = ['title', 'author', 'category', 'image', 'file', 'content']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入博客标题'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入作者名'}),
			'category': forms.Select(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'btn btn-default form-control'}),
			'file': forms.FileInput(attrs={'class': 'btn btn-default form-control', 'multiple': True}),#多文件上传
			'content': forms.Textarea(attrs={'cols': 50, 'rows': 10, 'class': 'form-control'}),
		}







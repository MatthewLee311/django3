from django import forms

class PostForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    postText = forms.CharField(label='Post', max_length=500)

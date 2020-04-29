from django import forms

class PostForm(forms.Form):
    postText = forms.CharField(label='Post', max_length=500)

class LoginForm(forms.Form):
    enteredUsername = forms.CharField(label='Username', max_length=25)
    enteredPassword = forms.CharField(label='Password', max_length=25)

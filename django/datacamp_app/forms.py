import email
from enum import unique
from django import forms
from django.contrib.auth.models import User
from datacamp_app.models import Topic, WebPage, UserProfileInfo

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = '__all__'


class WebPageForm(forms.ModelForm):

    class Meta:
        model = WebPage
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('portofolio','profile_picture')
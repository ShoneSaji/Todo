from django import forms
from work_app.models import User,Taskmodel

class Register(forms.ModelForm):
    class Meta: #class meta used to get these values

        model=User
        fields=["username","first_name","last_name","email","password"]
        widgets={
            # 'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),  #form-control is bootstrap class
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter lastname'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter valid email'}),
            # 'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password must be strong'})
        }



class TaskForm(forms.ModelForm):
    class Meta:

        model=Taskmodel
        fields=["task_name","task_description"]
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter a task here'}),
            'task_description':forms.Textarea(attrs={'class':'form-control','column':20,'rows':5,'placeholder':'enter a description'})
        }

class Login(forms.Form):

    username=forms.CharField()
    password=forms.CharField()          
    widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'})
        }
from django import forms
from . models import Signup


class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['first_name', 'last_name', 'email_address', 'user_name', 'password']
        
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border rounded-md text-gray-700 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'First Name'
            }),
            
            'last_name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border rounded-md text-gray-700 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Last Name'
            }),
            
            'email_address': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border rounded-md text-gray-700 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Email Address'
            }),
            
            'user_name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border rounded-md text-gray-700 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'User name'
            }),
            
            'password':forms.PasswordInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border rounded-md text-gray-700 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Password'
            })
        

        }

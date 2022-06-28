from typing import Any, Optional, Dict
from dataclasses import fields
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
            'avatar',
        )
    
    def clean_age(self) -> Optional[Dict[str, Any]]:
        age = self.cleaned_data.get('age')
        
        if age < 18:
            raise ValidationError('Вы слишком молоды')

        return age


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
            'avatar',
            
        )
    
    def clean_age(self) -> Optional[Dict[str, Any]]:
        age = self.cleaned_data.get('age')
        
        if age < 18:
            raise ValidationError('Вы слишком молоды')

        return age
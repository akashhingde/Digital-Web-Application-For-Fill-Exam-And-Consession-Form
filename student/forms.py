from django import forms
from django.contrib.auth import authenticate
from .models import *
from django.core.validators import validate_email
from django.contrib.auth.models import User

SUBJECTS_CHOICES = (
    ('one', 'ONE'),
    ('two', 'TWO'),
    ('three', 'THREE'),)

YEARS = [x for x in range(2019, 2020)]


class UserProfileform(forms.ModelForm):
    class Meta:
        model = UserProfileModel

        fields = ('full_name', 'gender', 'mobile_no',
                  'category', 'address', 'image')


class examform(forms.ModelForm):

    class Meta:

        model = examformmodel
        fields = ['month', 'roll_no', 'branch', 'year', 'semester']
		
        
	           

class atktform(forms.ModelForm):
    class Meta:
        model = atktmodel

        fields = ('month', 'roll_no', 'branch', 'year', 'semester', 'last_seat_no','IT_FE_1','IT_FE_2','IT_FE_3','IT_FE_4','IT_FE_5','IT_FE_6'
                  )


class regularrevalutionform(forms.ModelForm):
    class Meta:
        model = regularrevalutionmodel

        fields = ('month', 'roll_no', 'branch', 'year', 'semester', 'last_seat_no',
                  )


class atktrevalutionform(forms.ModelForm):
    class Meta:
        model = atktrevalutionmodel

        fields = ('month', 'roll_no', 'branch', 'year', 'semester', 'last_seat_no',
                  )


class regularphotocopyform(forms.ModelForm):
    class Meta:
        model = regularphotocopymodel

        fields = ('month', 'roll_no', 'branch', 'year', 'semester', 'last_seat_no',
                  )


class atktphotocopyform(forms.ModelForm):
    class Meta:
        model = atktphotocopymodel

        fields = ('month', 'roll_no', 'branch', 'year', 'semester', 'last_seat_no',
                  )


class concessionform(forms.ModelForm):

    class Meta:
        model = consessionformmodel
        fields = ('last_ticket_from', 'last_ticket_to', 'last_ticket_type',
                  'last_ticket_period', 'last_certificate_no', 'last_ticket_no', 'from_date')
        widgets = {'from_date': forms.SelectDateWidget(years=YEARS)}


class newconcessionform(forms.ModelForm):

    class Meta:
        model = newconsessionformmodel
        fields = ('ticket_from', 'ticket_to', 'ticket_type',
                  'ticket_period', 'from_date')
        widgets = {'from_date': forms.SelectDateWidget(years=YEARS)}


class uploadresultform(forms.ModelForm):

    class Meta:
        model = uploadresultmodel
        fields = ('branch', 'semester', 'result',)


class uploadnoticeform(forms.ModelForm):
    class Meta:
        model = uploadnoticemodel
        fields = ('branch', 'notice',)

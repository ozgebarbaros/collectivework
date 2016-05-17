# -*- coding:utf-8  -*-
import datetime

from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, ValidationError
from django.forms.widgets import TextInput, HiddenInput, Textarea, DateInput

from collectivework.models import Ticket, TicketTag

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ['creationdate','progress','assigneduser']
        widgets = {
           'title': TextInput(attrs={'class':'form-control'}),
           'short_desc': TextInput(attrs={'class':'form-control'}),
           'long_desc': Textarea(attrs={'class':'form-control'}),
           'enddate': DateInput(attrs={'id':'datepicker', 'class':'form-control pull-right'}),
           'requestinguser': HiddenInput(),
           'accepted': HiddenInput(),
           'rejected': HiddenInput(),
           'completed': HiddenInput(),
        }

# -*- coding:utf-8  -*-

from django.forms import ModelForm
from django.forms.widgets import TextInput, HiddenInput, Textarea, DateInput, SelectMultiple

from ticket.models import Ticket


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ['creation_date', 'progress', 'assigned_user', 'accepted', 'rejected', 'completed']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'short_desc': TextInput(attrs={'class': 'form-control'}),
            'long_desc': Textarea(attrs={'class': 'form-control'}),
            'end_date': DateInput(attrs={'id': 'datepicker', 'class': 'form-control pull-right'}),
            'tag': SelectMultiple(attrs={'class': 'form-control'}),
            'request_in_user': HiddenInput(),
            'accepted': HiddenInput(),
            'rejected': HiddenInput(),
            'completed': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateTicketForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
        self.fields['request_in_user'].required = False

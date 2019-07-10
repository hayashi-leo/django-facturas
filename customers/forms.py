# this file was manually created and not
# not automatically added by django during 'startapp'

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = ('companyName', 'contactName', 'contactTitle',
                  'address', 'city', 'region', 'postalCode',
                  'country', 'phone', 'fax', 'email',
                  'date_created', 'date_modified', )


class NewCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = ('companyName', 'contactName', 'contactTitle',
                  'address', 'city', 'region', 'postalCode',
                  'country', 'phone', 'fax', 'email',)

class EditCustomerForm(NewCustomerForm):
    pass


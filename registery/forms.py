from django import forms
from .models import POSITION_CHOICES, Employee


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('firstname', 'lastname', 'mobile', 'emp_no', 'position', 'place')
        labels = {
            'firstname':'First Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = POSITION_CHOICES
        self.fields['emp_no'].required = False
        self.fields['place'].required = False

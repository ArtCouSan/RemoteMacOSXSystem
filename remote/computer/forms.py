from django import forms
from computer.models import Computer

class ComputerForm(forms.Form):

    name = forms.CharField(required=True)
    ip = forms.CharField(required=True)
    user = forms.CharField(required=True)
    userLogin = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(ComputerForm, self).is_valid():
            self.add_error('Verifique os campos')
            valid = False

        return valid
        
        computer = Computer.objects.get(ip = self.data['ip'])

        if computer.ip:
            self.add_error('IP existente')
            valid = False

        return valid

    def add_error(self, message):
        erros = self._e.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorsList())
        error.append(message)
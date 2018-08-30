from django import  forms
from django.contrib.auth.models import Command

class CommandForm(forms.Form):

    category = forms.CharField(required=True)
    name = forms.CharField(required=True)
    command = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(CommandForm, self).is_valid():
            self.add_error('Verifique os campos')
            valid = False

        command_exists = Command.objects.filter(name=self.data['name']).exists()

        if command_exists:
            self.add_error('Comando existente')
            valid = false

        return valid

    def add_error(self, message):
        erros = self._e.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorsList())
        error.append(message)
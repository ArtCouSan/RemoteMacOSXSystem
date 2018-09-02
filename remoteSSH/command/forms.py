from django import  forms

class CommandForm(forms.Form):

    category = forms.CharField(required=True)
    name = forms.CharField(required=True)
    command = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(CommandForm, self).is_valid():
            self.add_error('Verifique os campos')
            valid = False
            
        return valid

    def add_error(self, message):
        erros = self._e.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorsList())
        error.append(message)
from atv.models.associacao import Associacao
from django import forms

from .validators import EmailInUseValidator, PasswordValidator


class PasswordField(forms.CharField):
    default_validators = [PasswordValidator]


class SubscribeForm(forms.Form):
    assoc_alias = forms.ModelChoiceField(
        label='Associação',
        queryset=Associacao.objects.all(),
        required=True,
        help_text='Se a sua associação não estiver cadastrada, entre em contato com a administração do Escoteirando')

    email = forms.EmailField(
        label="E-mail",
        required=True,
        help_text='Seu e-mail será utilizado para login',
        validators=[EmailInUseValidator]
    )

    password = PasswordField(
        label="Senha do usuário",
        widget=forms.PasswordInput(),
        help_text='Senha a ser utilizada pelo usuário',
        required=True,
    )

    chk_view_pass = forms.BooleanField(
        label="Visualizar senha",
        widget=forms.CheckboxInput()
    )

    assoc_user = forms.CharField(
        label="Usuário da associação",
        widget=forms.TextInput(),
        required=True
    )

    assoc_pass = forms.CharField(
        label="Senha da associação",
        widget=forms.PasswordInput(),
        help_text='Sua senha da associação não será armazenada. Consulte nossa política de privacidade.')

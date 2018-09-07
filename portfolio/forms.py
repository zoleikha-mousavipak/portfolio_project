from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=30,
                               required=False,
                               )

    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, required=False)


class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'size': '50'}))
    subject = forms.CharField(label="Subject", widget=forms.TextInput(attrs={'size': '50'}))
    message = forms.CharField(label="Message", widget=forms.Textarea, required=True)
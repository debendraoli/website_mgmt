from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32, widget=forms.TextInput(
        attrs=
        {'id': 'name',
         'class': 'form-control',
         'placeholder': 'Enter your name'}))

    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs=
        {'id': 'email',
         'class': 'form-control',
         'placeholder': 'Enter your email'}))

    subject = forms.CharField(label='Subject', max_length=80, widget=forms.TextInput(
        attrs=
        {'id': 'subject',
         'class': 'form-control',
         'placeholder': 'Subject'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(
        attrs=
        {'id': 'message',
         'class': 'form-control',
         'placeholder': 'Enter your message',
         'rows': '1'}
    ))

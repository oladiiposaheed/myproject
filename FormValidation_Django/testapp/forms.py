from django import forms
from django.core import validators
class FeedbackForm(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(label='Enter Password:', widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)', widget=forms.PasswordInput)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    #feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('Total Form Validation')
        total_cleaned_data = super().clean()  #get all data enter by the end user
        print('Validating Name')
        inputname = total_cleaned_data['name']
        if len(inputname) < 4:
            raise forms.ValidationError('The Minimum number of characters in the name field should be 4')
        if inputname[0].lower() != 's':
            raise forms.ValidationError('Name should starts with s or S')

        inputmail = total_cleaned_data['email']
        print('Validating Email')
        if inputmail[-10:] != '@gmail.com' and inputmail[-10:] != '@yahoo.com':
            raise forms.ValidationError('gmail extension should be gmail or yahoo')

        pwd = total_cleaned_data['password']    #value entered for the password Field
        rpwd = total_cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError('Both passwords must be same')

        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError('Hello BOT how are you')

from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    ROLE = (
        ('student', 'Student'),
        ('professor', 'Professor'),
    )
    role = forms.ChoiceField(choices=ROLE, required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user
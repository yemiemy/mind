# from django.contrib.auth.models import User
# from django.contrib.auth.forms import PasswordResetForm

# from allauth.account.forms import SignupForm
# from allauth.account.adapter import DefaultAccountAdapter
# from django import forms
# from accounts.models import UserProfile, Institution
# from django.shortcuts import redirect
# from django.contrib import messages

# class CustomSignupForm(SignupForm):

#     first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control" }))

#     last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control" }))

#     phone = forms.IntegerField(label='Phone', widget=forms.NumberInput(attrs={"placeholder": "Phone", "class": "form-control" }))

#     institution = forms.ModelChoiceField(Institution.objects.all(), widget=forms.Select(attrs={"class": "form-control" }))

#     faculty = forms.CharField(label='Faculty', widget=forms.TextInput(attrs={"placeholder": "Faculty", "class": "form-control" }))

#     department = forms.CharField(label='Department', widget=forms.TextInput(attrs={"placeholder": "Department", "class": "form-control" }))

#     level = forms.IntegerField(label='Level', widget=forms.NumberInput(attrs={"placeholder": "Level", "class": "form-control" }))

#     photo = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control" }), required=True)

#     description = forms.CharField(label='About Me', widget=forms.TextInput(attrs={"placeholder": "About Me", "class": "form-control" }))
    

#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()

#         return user

# class UserAccountAdapter(DefaultAccountAdapter):

#     def save_user(self, request, user, form, commit=True):
#         """
#         This is called when saving user via allauth registration.
#         We override this to set additional data on user object.
#         """
#         # Do not persist the user yet so we pass commit=False
#         # (last argument)
#         user = super(UserAccountAdapter, self).save_user(request, user, form, commit=False)

#         user.save()
        
#         profile = UserProfile()
#         profile.user = user
#         profile.phone = form.cleaned_data['phone']
#         profile.institution = form.cleaned_data['institution']
#         profile.faculty = form.cleaned_data['faculty']
#         profile.department = form.cleaned_data['department']
#         profile.level = form.cleaned_data['level']
#         profile.description = form.cleaned_data['description']
#         profile.photo = form.cleaned_data['photo']
        
#         profile.save()
    

# # class EmailValidationOnForgotPassword(PasswordResetForm):

# #     def clean_email(self):
# #         email = self.cleaned_data['email']
# #         if not User.objects.filter(email__iexact=email, is_active=True).exists():
# #             msg = ("There is no user registered with the specified E-Mail address. Check the E-Mail and try again.")
# #             self.add_error('email', msg)
# #         return email
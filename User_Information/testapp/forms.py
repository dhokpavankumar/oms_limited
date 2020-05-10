from django import forms
from testapp.models import student


class SignupForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','mobile_number','email','userID']

    def clean_name(self):  # Validates the Name Field
         name = self.cleaned_data['name']
         words=name.split(' ')
         if len(words) < 3:
             raise forms.ValidationError('This field cannot be left blank')
         return name
    #
    # def clean_mobileNO(self):  # Validates the Name Field
    #     mobileNO = self.cleaned_data.get('mobile_number')
    #     if max():
    #         raise forms.ValidationError('This field cannot be left blank')
    #     return mobileNO

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    mobile_number = forms.IntegerField()
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Reenter Password', widget=forms.PasswordInput)


def clean(self):
    total_cleaned_data=super().clean()
    pwd=total_cleaned_data['password']
    rpwd=total_cleaned_data['rpassword']

    if pwd != rpwd:
        raise forms.ValidationError('Both Passwords must be same')
#

#     except student.DoesNotExist:
#         # Unable to find a user, this is fine
#         return email
#
#         # A user was found with this as a username, raise an error.
#     raise forms.ValidationError('This email address is already in use.')


# def clean(self):
#         match_email = student.objects.get(email='email')
#         match_mo_no = student.objects.get(mobile_number='mobile_number')
#         total_clean_data=super().clean()
#         input_email=total_clean_data['email']
#
#         if input_email==match_email:
#             raise forms.ValidationError('This email address is already in use.')
#
#         input_mobile_no=total_clean_data['mobile_number']
#         if input_mobile_no == match_mo_no:
#             raise forms.ValidationError('This Mobile number is already in use.')


from django import forms
from captcha.fields import CaptchaField

class CaptchaForm(forms.Form):
    myfield = AnyOtherField()
    captcha = CaptchaField()

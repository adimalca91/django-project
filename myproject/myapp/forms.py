from django import forms
from .models import Logger, Booking

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'

# WORK_SHIFTS = (
#     ("1", "Morning"),
#     ("2", "Afternoon"),
#     ("3", "Evening"),
# )

# class InputForm(forms.Form):
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     shift = forms.ChoiceField(choices=WORK_SHIFTS)
#     time_log = forms.TimeField()
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        
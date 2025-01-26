from django import forms

class GroupForm(forms.Form):
    foreign_count = forms.IntegerField(label="外国人の人数", min_value=0)
    japanese_count = forms.IntegerField(label="日本人の人数", min_value=0)
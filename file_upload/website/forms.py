from django.forms import ModelForm, ValidationError
from django import forms
from website.models import Moment


class UserForm(forms.Form):
    user_name = forms.CharField()
    user_info = forms.FileField()


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'

    def clean(self):
        cleaned_data = super(MomentForm, self).clean()
        content = cleaned_data.get("content")
        if content is None:
            raise ValidationError("请输入Content内容！")
        elif content.find("ABCD") >= 0:
            raise ValidationError("不能包含敏感字ABCD！")
        return cleaned_data

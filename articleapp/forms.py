from projectapp.models import Project
from django.forms import ModelForm
from articleapp.models import Article
from django import forms


class ArticleCreationForm(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "editable", "style": "height: auto;"})
    )
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ["title", "image", "project", "content"]

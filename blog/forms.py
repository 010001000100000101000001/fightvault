from django import forms
from .models import Rating, Comment


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

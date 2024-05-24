from django import forms
from .models import Rating, Comment, Vote


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['choice']
        widgets = {
            'choice': forms.RadioSelect(choices=[('fighter1', 'Fighter 1'), ('fighter2', 'Fighter 2')]),
        }

from django.contrib import admin
from .models import Post, Comment, Rating, Vote
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    fields = (
        'title', 'slug', 'author', 'content', 'featured_image', 'status',
        'excerpt', 'fighter1_name', 'fighter2_name'
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on', 'approved')
    list_filter = ('approved', 'created_on',)
    search_fields = ('post__title', 'author__username', 'body')
    date_hierarchy = 'created_on'
    readonly_fields = ('created_on',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'score', 'created_on')
    list_filter = ('score', 'created_on',)
    search_fields = ('post__title', 'user__username')
    readonly_fields = ('created_on',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'choice', 'created_at')
    list_filter = ('choice', 'created_at',)
    search_fields = ('post__title', 'user__username')
    readonly_fields = ('created_at',)

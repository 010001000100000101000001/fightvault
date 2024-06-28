from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('custom-logout/', views.custom_logout, name='custom_logout'),
    path('<slug:slug>/', views.get_post_detail, name='post_detail'),
    path('rate-post/<int:post_id>/', views.rate_post, name='rate_post'),
    path(
        'edit-comment/<int:comment_id>/',
        views.edit_comment, name='edit_comment'),
]

from django.db import models
from django.contrib.auth.models import User

# Constants for post status choices
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (CharField): The title of the post (must be unique).
        slug (SlugField): The URL-friendly version of the title (must be unique).
        author (ForeignKey): The author of the post, linked to a User instance.
        content (TextField): The main content of the post.
        created_on (DateTimeField): The date and time when the post was created (auto-populated).
        updated_on (DateTimeField): The date and time when the post was last updated (auto-populated).
        status (IntegerField): The status of the post (0 for Draft, 1 for Published).
        excerpt (TextField): A short summary or teaser of the post (optional).
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a string representation of the post, which is the title.
        """
        return self.title


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (ForeignKey): The post the comment is related to (many-to-one relationship).
        author (ForeignKey): The author of the comment, linked to a User instance.
        body (TextField): The content of the comment.
        approved (BooleanField): Whether the comment is approved (default is False).
        created_on (DateTimeField): The date and time when the comment was created (auto-populated).
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the comment, including the author's username
        and the comment's content.
        """
        return f"Comment by {self.author.username}: {self.body[:20]}..."

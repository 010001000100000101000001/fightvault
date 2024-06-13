from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Constants for post status choices
STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Published"),
)


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (CharField): The title of the post (must be unique).
        slug (SlugField): The URL-friendly version of the title
        (must be unique).
        author (ForeignKey): The author of the post, linked to a User instance.
        content (TextField): The main content of the post.
        created_on (DateTimeField): The date and time when the post was created
        (auto-populated).
        updated_on (DateTimeField): The date and time when the post was last
        updated (auto-populated).
        status (IntegerField): The status of the post (0 for Draft, 1 for
        Published).
        excerpt (TextField): A short summary or teaser of the post (optional).
        fighter1_name (CharField): Name of the first fighter associated with
        the post.
        fighter2_name (CharField): Name of the second fighter associated with
        the post.
        display_voting (BooleanField): Flag indicating if voting is displayed
        for the post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    excerpt = models.TextField(blank=True)
    fighter1_name = models.CharField(max_length=35, default='Fighter 1')
    fighter2_name = models.CharField(max_length=35, default='Fighter 2')
    display_voting = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of the post.
        """
        return f"{self.title} | written by {self.author.username}"


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (ForeignKey): The post the comment is related to
        (many-to-one relationship).
        author (ForeignKey): The author of the comment, linked to a User
        instance.
        body (TextField): The content of the comment.
        approved (BooleanField): Whether the comment is approved
        (default is False).
        created_on (DateTimeField): The date and time when the comment was
        created (auto-populated).
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_author"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns a string representation of the comment.
        """
        return f"Comment by {self.author.username}: {self.body[:20]}..."


class Rating(models.Model):
    """
    Represents a rating on a blog post.

    Attributes:
        post (ForeignKey): The post being rated (many-to-one relationship).
        user (ForeignKey): The user who submitted the rating.
        score (IntegerField): The star rating (1-5).
        comment (TextField): Optional review comment.
        created_on (DateTimeField): When the rating was submitted.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="ratings"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    score = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )  # 1 to 5 stars (gloves)
    comment = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        """
        Returns a string representation of the rating.
        """
        return (
                f"Rating by {self.user.username} on {self.post.title}: "
                f"{self.score} stars"
                )


class Vote(models.Model):
    """
    Represents a vote on a blog post.

    Attributes:
        post (ForeignKey): The post being voted on (many-to-one relationship).
        user (ForeignKey): The user who submitted the vote.
        choice (CharField): The choice made in the vote ('fighter1' or
        'fighter2').
        created_at (DateTimeField): When the vote was submitted.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        """
        Returns a string representation of the vote.
        """
        return (
            f"{self.user.username} voted for {self.choice} "
            f"on {self.post.title}"
        )

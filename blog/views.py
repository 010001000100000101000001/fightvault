from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import generic
from .models import Post, Rating

# Class based views


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    View function to display a single blog post and its ratings.

    Args:
        request (HttpRequest): The request object.
        slug (str): The URL-friendly identifier for the post.

    Returns:
        HttpResponse: An HTTP response object containing the rendered post detail template.
    """
    # Fetch the blog post and raise a 404 error if not found
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Retrieve all ratings for the post
    ratings = post.ratings.all()

    # Calculate average rating if there are any ratings; otherwise set to 0
    average_rating = sum(rating.score for rating in ratings) / len(ratings) if ratings else 0

    # Render the post_detail template with context variables
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "ratings": ratings,
            "average_rating": average_rating,
        }
    )

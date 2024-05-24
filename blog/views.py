from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import logout
from .models import Post, Rating, Comment, Vote
from .forms import RatingForm, CommentForm, VoteForm

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

    # Retrieve all comments for the post, ordered by creation date
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

vote_form = VoteForm()#
if request.method == "POST" and 'vote' in request.POST:
    vote_form = VoteForm(request.POST)
    if vote_form.is_valid():
        vote = vote_form.save(commit=False)
        vote.post = post
        vote.user = request.user
        vote.save()
        messages.success(request, "Your vote has been submitted.")
        return redirect('post_detail', slug=post.slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment was submitted successfully and is currently waiting admin approval.'
            )
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    # Render the post_detail template with context variables
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "ratings": ratings,
            "average_rating": average_rating,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def custom_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home page

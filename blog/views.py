from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
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

    # Initialize vote form
    vote_form = VoteForm()

    # Calculate vote percentages
    total_votes = post.votes.count()
    if total_votes > 0:
        fighter1_votes = post.votes.filter(choice='fighter1').count()
        fighter2_votes = post.votes.filter(choice='fighter2').count()
        fighter1_percentage = round((fighter1_votes / total_votes) * 100, 2)
        fighter2_percentage = round((fighter2_votes / total_votes) * 100, 2)
    else:
        fighter1_percentage = 0
        fighter2_percentage = 0


    if request.method == "POST" and 'vote' in request.POST:
        if not request.user.is_authenticated:
            messages.warning(request, "You need to log in or register to vote.")
            return redirect('post_detail', slug=post.slug)
        vote_form = VoteForm(request.POST)
        if vote_form.is_valid():
            # Check if the user has already voted on this post
            existing_vote = Vote.objects.filter(post=post, user=request.user).first()
            if existing_vote:
                messages.error(request, "You have already voted on this post.")
            else:
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
            "vote_form": vote_form,
            "fighter1_percentage": fighter1_percentage,
            "fighter2_percentage": fighter2_percentage,
            "fighter1_name": post.fighter1_name,
            "fighter2_name": post.fighter2_name,
        }
    )

@require_POST
@login_required
def rate_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    rating_value = request.POST.get('rating')

    if not rating_value:
        return JsonResponse({'message': 'Rating value is required.'}, status=400)

    rating_value = int(rating_value)
    if rating_value < 1 or rating_value > 5:
        return JsonResponse({'message': 'Invalid rating value.'}, status=400)

    rating, created = Rating.objects.get_or_create(
        post=post,
        user=request.user,
        defaults={'score': rating_value}
    )

    if not created:
        return JsonResponse({'message': 'You have already rated this post.'}, status=400)

    return JsonResponse({'message': 'Thank you for rating this post!'})

def custom_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home page

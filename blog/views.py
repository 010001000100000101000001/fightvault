from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Post, Rating, Comment, Vote
from .forms import RatingForm, CommentForm, VoteForm
from django.urls import reverse


# Class based views
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def get_post_detail(request, slug):
    """
    View function to display a single blog post and its ratings.
    """
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)

    ratings = post.ratings.all()
    average_rating = calculate_average_rating(ratings)

    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    vote_form = VoteForm()
    comment_form = CommentForm()

    fighter1_percentage, fighter2_percentage = calculate_vote_percentages(post)

    if request.method == "POST":
        if 'vote' in request.POST:
            return handle_vote_post(request, post, vote_form)
        elif 'rating' in request.POST:
            return handle_rating_post(request, post)
        else:
            return handle_comment_post(request, post, comment_form)

    return render_post_detail(request, post, ratings, average_rating, comments,
                              comment_count, comment_form, vote_form,
                              fighter1_percentage, fighter2_percentage)


def calculate_average_rating(ratings):
    """
    Function to calculate the average rating from a queryset of ratings.
    """
    if ratings:
        total_score = sum(rating.score for rating in ratings)
        return round(total_score / len(ratings), 1)
    return 0


def calculate_vote_percentages(post):
    """
    Function to calculate the percentage of votes for fighter1 and fighter2.
    """
    total_votes = post.votes.count()
    if total_votes > 0:
        fighter1_votes = post.votes.filter(choice='fighter1').count()
        fighter2_votes = post.votes.filter(choice='fighter2').count()
        fighter1_percentage = round((fighter1_votes / total_votes) * 100)
        fighter2_percentage = round((fighter2_votes / total_votes) * 100)
    else:
        fighter1_percentage = 0
        fighter2_percentage = 0
    return fighter1_percentage, fighter2_percentage


def handle_vote_post(request, post, vote_form):
    """
    Function to handle voting on a post.
    """
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in or register to vote")
        return redirect('post_detail', slug=post.slug)

    vote_form = VoteForm(request.POST)
    if vote_form.is_valid():
        existing_vote = (
            Vote.objects
            .filter(post=post, user=request.user)
            .first()
        )
        if existing_vote:
            messages.error(request, "You have already voted on this post.")
        else:
            vote = vote_form.save(commit=False)
            vote.post = post
            vote.user = request.user
            vote.save()
            messages.success(request, "Your vote has been submitted.")
        return redirect('post_detail', slug=post.slug)


def handle_rating_post(request, post):
    """
    Function to handle rating submission on a post.
    """
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in or register to rate")
        return redirect('post_detail', slug=post.slug)

    rating_value = request.POST.get('rating')
    if rating_value:
        try:
            rating_value = int(rating_value)
            if 1 <= rating_value <= 5:
                save_or_update_rating(post, request.user, rating_value)
                messages.success(request, "Your rating has been submitted.")
            else:
                messages.error(request, "Invalid rating value.")
        except ValueError:
            messages.error(
                request, "Invalid rating value. Must be an integer."
            )
    return redirect('post_detail', slug=post.slug)


def save_or_update_rating(post, user, rating_value):
    rating, created = Rating.objects.get_or_create(
        post=post,
        user=user,
        defaults={'score': rating_value}
    )
    if not created:
        rating.score = rating_value
        rating.save()


def handle_comment_post(request, post, comment_form):
    """
    Function to handle commenting on a post.
    """
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        messages.success(
            request,
            'Your comment was submitted and is waiting admin approval.'
        )
    return redirect('post_detail', slug=post.slug)


def render_post_detail(request, post, ratings, average_rating, comments,
                       comment_count, comment_form, vote_form,
                       fighter1_percentage, fighter2_percentage):
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


@login_required
def edit_comment(request, comment_id):
    """
    View to edit an existing comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    # Check the user is the author of the comment
    if comment.author != request.user:
        messages.error(request, "This is not your comment.")
        return redirect('post_detail', slug=comment.post.slug)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment has been updated.")
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(
        request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check that the user is the author of the comment
    if comment.author != request.user:
        messages.error(
            request, "You are not authorised to delete this comment.")
        return redirect('post_detail', slug=comment.post.slug)

    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect('post_detail', slug=comment.post.slug)


@login_required
def rate_post(request, post_id):
    """
    View function to handle rating a post via HTTP POST request.
    """
    post = get_object_or_404(Post, id=post_id)
    rating_value = request.POST.get('rating')

    if not rating_value:
        return HttpResponse('Rating value is required.', status=400)

    try:
        rating_value = int(rating_value)
        if rating_value < 1 or rating_value > 5:
            return HttpResponse(
                'Invalid rating value. Must be between 1 and 5.', status=400)

        save_or_update_rating(post, request.user, rating_value)

        average_rating = post.ratings.aggregate(Avg('score'))['score__avg']
        message = f"Your rating ({rating_value}) has been submitted."
        messages.success(request, message)

        return redirect('post_detail', slug=post.slug)

    except ValueError:
        messages.error(request, 'Invalid rating value. Must be an integer.')
        return redirect('post_detail', slug=post.slug)


def save_or_update_rating(post, user, rating_value):
    rating, created = Rating.objects.get_or_create(
        post=post,
        user=user,
        defaults={'score': rating_value}
    )
    if not created:
        rating.score = rating_value
        rating.save()


def custom_logout(request):
    """
    View function to log out the current user.
    """
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

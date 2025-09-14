from django.shortcuts import render
from movies.models import Review

def index(request):
    # Get all reviews ordered by likes descending
    top_reviews = Review.objects.select_related('user').order_by('-likes')[:20]
    return render(request, 'top_review/index.html', {'top_reviews': top_reviews})

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

@require_POST
def like_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.likes += 1
    review.save()
    return redirect('top_review.index')
    
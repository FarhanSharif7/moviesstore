def index(request):
from django.shortcuts import render
from movies.models import Review
def index(request):
    # Get all reviews ordered by likes descending
    top_reviews = Review.objects.select_related('user').order_by('-likes')[:20]
    return render(request, 'top_review/index.html', {'top_reviews': top_reviews})

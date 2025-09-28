from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import petition
from .models import Petition
from .forms import PetitionForm

def index(request):
    petition = Petition.objects.annotate(num_votes=Count('signatures')).order_by('-num_votes', '-created_at')
    return render(request, 'petition/index.html', {'petitions': petition})


@login_required
def create_petition(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            return redirect('petition.index')
    else:
        form = PetitionForm()
    return render(request, 'petition/create_petition.html', {'form': form})

@login_required
def vote(request, petition_id) :
    petition = get_object_or_404(Petition, id=petition_id)
    petition.signatures.add(request.user)
    return redirect('petition.index')

@login_required
def unvote(request, petition_id) :
    petition = get_object_or_404(Petition, id=petition_id)
    petition.signatures.remove(request.user)
    return redirect('petition.index')

@login_required
def edit_petiton(request, petition_id):
    petition = get_object_or_404(Petition, id = petition_id)
    if request.user != petition.created_by:
        return redirect('petition.index')
    if request.method == 'POST':
        form = PetitionForm(request.POST, instance=petition)
        if form.is_valid():
            form.save()
            return redirect('petition.index')
    else:
        form = PetitionForm(instance=petition)
    return render(request, 'petition/create_petition.html', {'form': form, 'editing' : True, 'petition': petition})

@login_required
def delete_petition(request, petition_id):
    petition = get_object_or_404(Petition, id = petition_id)
    if request.user != petition.created_by:
        return redirect('petition.index')
    if request.method == 'POST':
        petition.delete()
        return redirect('petition.index')
    return render(request, 'petition/create_petition.html', {'form': PetitionForm(instance=petition), 'confirm_delete' : True, 'petition': petition})
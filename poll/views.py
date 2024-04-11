from .forms import SignupForm
from .forms import CreatePollForm
from .models import Poll, Vote
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth import login, authenticate
from django.db.models import F, ExpressionWrapper, FloatField


@login_required
def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls,
        'user_authenticated': True  
    }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            if poll.deadline and poll.deadline < timezone.now():
                pass
            else:
                poll.save()
                return redirect('home') 
    else:
        form = CreatePollForm()
    return render(request, 'poll/create_poll.html', {'form': form})

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    
    if poll.deadline and poll.deadline < timezone.now():
        return render(request, 'poll/voting_closed.html', {'poll': poll})
    
    
    already_voted = Vote.objects.filter(user=request.user, poll=poll).exists()

    if request.method == 'POST' and not already_voted:
        selected_option = request.POST.get('poll')
        if selected_option:
            if selected_option == 'option1':
                poll.option_one_count += 1
            elif selected_option == 'option2':
                poll.option_two_count += 1
            elif selected_option == 'option3':
                poll.option_three_count += 1
            poll.save()

            Vote.objects.create(user=request.user, poll=poll)
            return redirect('home')

    return render(request, 'poll/votes.html', {'poll': poll, 'already_voted': already_voted})

@login_required
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    total_votes = poll.option_one_count + poll.option_two_count + poll.option_three_count
    
    poll.option_one_percentage = round((poll.option_one_count * 100.0) / total_votes, 2) if total_votes != 0 else 0
    poll.option_two_percentage = round((poll.option_two_count * 100.0) / total_votes, 2) if total_votes != 0 else 0
    poll.option_three_percentage = round((poll.option_three_count * 100.0) / total_votes, 2) if total_votes != 0 else 0
    
    context = {
        'poll': poll,
        'total_votes': total_votes,
    }
    return render(request, 'poll/poll_results.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'poll/signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'poll/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return render(request, 'poll/logout.html')

@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll.delete()
    return redirect('home')

@login_required
def view_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {'poll': poll}
    return render(request, 'poll/view_poll.html', context)

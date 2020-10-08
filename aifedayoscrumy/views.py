from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
import random
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User, Group



###############################################################################################
#                         C R E A T I N G   S U P E R  U S E R S                              #
###############################################################################################    
def base(request):
    return render(request, 'home.html')

def index(request):

    if request.method == 'POST':
        #Form was submitted
        form = SignUpForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            my_group = Group.objects.get(name = 'Developer')
            post.user = User.objects.create_superuser(
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email = request.POST.get('email'),
                username = request.POST.get('username'),
                password = request.POST.get('password'))
            my_group.user_set.add(post.user)
        # Form field passed validation
            post.user.save()
            
        return render(request, 'success.html', {'form' : form})  
        
    else:
        form = SignUpForm()
    return render(request, 'aifedayoscrumy/index.html', {'form' : form})  
    #return HttpResponse("This is a Scrum Application")

###############################################################################################
#        D I S P L A Y I N G  I N D I V I D U A L  G O A L  A T T R I B U T E S               #
###############################################################################################  


def goal_detail(request, goal_id):
    post = get_object_or_404(ScrumyGoals, goal_id = goal_id)
    return render(request, 'aifedayoscrumy/goal_detail.html', {'post' : post})
    
    
###############################################################################################
#        H O M E  P A G E  F O R  D I S P L A Y I N G  U S E R S'  G O A L S                  #
###############################################################################################  

def home(request):
    #obj2 = ScrumyGoals.objects.filter(goal_name__startswith = 'Keep Learning Django')
    #output = ", ".join([eachgoal.goal_name for eachgoal in obj2])
    
    users = User.objects.all()
    
    context = {
            'users' : users,       
   }
    #return HttpResponse(output)

    return render(request, 'aifedayoscrumy/home.html', context)

###############################################################################################
#                         C R E A T I N G   G O A L S  A S  P E R  U S E R S                  #
###############################################################################################    
def add_goal(request):
    
    user = request.user
    goal_status  = GoalStatus.objects.all()
    # Aasigning a value to the currently logged in user
    sample_dict = {}
    # Creating a dic to store the random values to avoid repitition
    number = random.randint(1000, 9999)
    if number not in sample_dict:
        sample_dict[number] = number
    if User.objects.filter(username = user, groups__name = 'Owner').exists() or \
        User.objects.filter(username = user, groups__name = 'Developer').exists() or \
        User.objects.filter(username = user, groups__name = 'Quality Assurance').exists():
        if request.method == "POST":
            form = CreateGoalForm(request.POST)
            if form.is_valid():
                post = form.save(commit = False)
                if post.user == request.user:
                    if post.goal_status == GoalStatus.objects.get(status_name = 'Weekly Goal'):
                        post.goal_id = number
                        post.save()
                        return redirect('goal_detail', goal_id = post.goal_id)
                    else:
                        return render(request, 'move_error.html', {})
                else:
                    return render(request, 'user_error.html', {})
        else:
            form = CreateGoalForm()
        return render(request, 'aifedayoscrumy/addgoal.html', {'form' : form})       
    else:
        form = CreateGoalForm()
    return render(request, 'aifedayoscrumy/addgoal.html', {'form' : form})

        



###############################################################################################
#                         M O V I N G   G O A L S  A S  P E R  U S E R S                      #
###############################################################################################
def move_goal(request, goal_id):
    
    user = request.user
    post = get_object_or_404(ScrumyGoals, goal_id = goal_id)
    if User.objects.filter(username = user, groups__name = 'Developer').exists():
        
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance = post )
            if post.user == request.user:
                if form.is_valid():
                    if GoalStatus.objects.get(status_name = 'Done Goal') != post.goal_status:
                        post = form.save(commit = False)
                        post.save()
                        return redirect('goal_detail', goal_id = post.goal_id)
                    else:
                         return render(request, 'move_error.html', {})
            else:
                return render(request, 'user_error.html', {})
        else:
            form = MoveGoalForm(instance=post)
        return render(request, 'aifedayoscrumy/move_goal.html', {'form' : form, 'post' : post})

    elif User.objects.filter(username = user, groups__name = 'Quality Assurance').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance = post )
            if form.is_valid():
                post = form.save(commit = False)
                post.save()
                return redirect('goal_detail', goal_id = post.goal_id)
                
        else:
            form = MoveGoalForm(instance=post)
        return render(request, 'aifedayoscrumy/move_goal.html', {'form' : form, 'post' : post})

    elif User.objects.filter(username = user, groups__name = 'Admin').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance = post )
            if form.is_valid():
                post = form.save(commit = False)
                post.save()
                return redirect('goal_detail', goal_id = post.goal_id)
                
        else:
            form = MoveGoalForm(instance=post)
        return render(request, 'aifedayoscrumy/move_goal.html', {'form' : form, 'post' : post})

    elif User.objects.filter(username = user, groups__name = 'Owner').exists():
        
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance = post )
            if post.user == request.user:
                if form.is_valid():
                    post = form.save(commit = False)
                    post.save()
                    return redirect('goal_detail', goal_id = post.goal_id)
            
            else:
                return render(request, 'user_error.html', {})
        else:
            form = MoveGoalForm(instance=post)
        return render(request, 'aifedayoscrumy/move_goal.html', {'form' : form, 'post' : post})
    else:
        form = MoveGoalForm(instance=post)
    return render(request, 'aifedayoscrumy/move_goal.html', {'form' : form, 'post' : post})






   
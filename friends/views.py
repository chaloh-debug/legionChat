from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import Profile

# Create your views here.
class friends(TemplateView):
    template_name="friends/friends.html"

def requests(context):
    allUsers = User.objects.all()

    return render(context, 'friends/requests.html', {"allUsers": allUsers})

@login_required
def profile(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Profile.objects.get(pk=user_id)
    except Profile.DoesNotExist:
        return HttpResponse("Profile does not exist!")
    
        
    is_self = True
    is_friend = False
    user = request.user.id
    if user != account:
        is_self = False
    elif user == account:
        is_self = True

    context['id'] = account.id
    context['username'] = account.user.username
    context['email'] = account.user.email
    context['avatar'] = account.avatar.url
    context['bio'] = account.bio

    context['is_self'] = is_self
    context['is_friend'] = is_friend

    return render(request, "friends/profile.html", context)
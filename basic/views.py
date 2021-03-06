from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from basic.models import Book
from basic.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = RequestContext(request)
    newest_books = Book.objects.order_by('shelf_date')[:5]
    context_dict = {
            'msg': 'Welcome!!',
            'newest_books': newest_books,
            }
    return render_to_response('basic/index.html', context_dict, context)


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
         user_form = UserForm()
         profile_form = UserProfileForm()

    return render_to_response(
             'basic/register.html',
             {'user_form': user_form, 'profile_form': profile_form,
                 'registered': registered},
             context)

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/basic/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('basic/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/basic/')

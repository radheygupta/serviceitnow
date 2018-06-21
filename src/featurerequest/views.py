from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import LoginForm, FeatureForm
from .models import Features
from .utils import reorder_priorties


@login_required
def index(request, page=1):
    latest_feature_list = Features.objects.filter().order_by('-target_date')
    paginator = Paginator(latest_feature_list, 10)

    try:
        feature_list = paginator.page(page)
    except PageNotAnInteger:
        feature_list = paginator.page(1)  # show first page if page is not PageNotAnInteger
    except EmptyPage:
        feature_list = paginator.page(paginator.num_pages)

    startPoint = 1
    endPoint = feature_list.paginator.num_pages

    if feature_list.paginator.num_pages > 10:
        if feature_list.number < 6:
            startPoint = 1
            endPoint = 10
        elif feature_list.number + 4 >= feature_list.paginator.num_pages:
            startPoint = feature_list.paginator.num_pages - 9
            endPoint = feature_list.paginator.num_pages
        else:
            startPoint = feature_list.number - 5
            endPoint = feature_list.number + 4

    pageList = range(startPoint, endPoint + 1)

    return render(request, 'featurerequest/index.html', {'feature_list': feature_list, 'pageList': pageList})


@login_required
def add_features(request):
    feature_form = FeatureForm(request.POST or None)
    if request.method == 'POST':
        if feature_form.is_valid():
            client = feature_form.cleaned_data['client']
            priority = feature_form.cleaned_data['priority']
            reorder_priorties(client, priority)
            feature_form.save()
            messages.success(request, 'The Feature request was succesfully created!.')
            return redirect('/features/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        feature_form = FeatureForm()
        return render(request, 'featurerequest/addfeatures.html', {'feature_form': feature_form})


def userlogin(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # print("{}:{}".format(username, password))
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # print("User logged in : {}".format(user.username))
                return redirect('/features/')
    # print("User login failed")
    return render(request, 'featurerequest/login.html', {'login_form': form})


def userlogout(request):
    logout(request)
    return redirect('/features/')

from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from captcha.fields import CaptchaField



def results(request):
    return render(request, "result.html", )


def index(request):
    if request.method == "POST":
        username = request.POST['myusername']
        password = request.POST['mypassword']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/results/")

    return render(request, "index.html", )


def Logout(request):
    logout(request)
    return redirect("/")


def registeracc(request):
    if request.method == "POST":
        username = request.POST['login']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Hasła się nie są identyczne')
            return render(request, "registeracc.html")
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            return redirect("/")

        except:
            pass

    return render(request, "registeracc.html")


def changepass(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.id
    if request.method == "POST":
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=username)
            u.set_password(new_password)
            u.save()
            return redirect("/")
        except:
            pass
    return render(request, "changepass.html")


def positions(request):
    pos = Positions.objects.all()
    if request.method == "POST":
        newpos = request.POST['poz']
        try:
            posss = Positions.objects.create(position_name=newpos)
            posss.save()
            return redirect("positions")
        except:
            pass

    return render(request, "positions.html", {'pos':pos})


def candidates(request):
    pos = Positions.objects.all()
    cos = Candidates.objects.all()
    if request.method == "POST":
        newcos = request.POST['coz']
        print(newcos)
        newpos = request.POST['poz']
        print(newpos)
        try:
            coss = Candidates.objects.create(candidate_name=str(newcos), candidate_position=str(newpos), candidate_votes=int(0))
            coss.save()
            return redirect("candidates")
        except:
            pass

    return render(request, "candidates.html", {'pos':pos, 'cos':cos})


def positionsDelete(request, mypos):
    posi = Positions.objects.filter(position_name=mypos)
    posi.delete()
    return redirect("positions")


def candidatesDelete(request, mycos):
    posi = Candidates.objects.filter(candidate_name=mycos)
    posi.delete()
    return redirect("candidates")


def results(request):
    cos = Candidates.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cos, 2)
    try:
        cos = paginator.page(page)
    except PageNotAnInteger:
        cos = paginator.page(1)
    except EmptyPage:
        cos = paginator.page(paginator.num_pages)

    if request.method == "POST":
        ask = request.POST['ask']
        print(ask)
        if ask is not None:
            cos = Candidates.objects.filter(candidate_name=ask)
    return render(request, "result.html", {'cos':cos})


def vote(request):
    cos = Candidates.objects.all()
    username = None
    if Votes is not None:
        if request.user.is_authenticated:
            username = request.user.username
            try:
                v = Votes.objects.filter(voter_id=username)
                tab = []
                for x in v:
                    tab.append(x.position)
                for t in tab:
                    vos = Votes.objects.get(voter_id=username, position=t)
                    pos = vos.position
                    print(pos)
                    cos = cos.exclude(candidate_position=pos)
            except Votes.DoesNotExist:
                vos = None
    return render(request, "vote.html", {'cos':cos})


def makevote(request, mycos, mypos):
    cos = Candidates.objects.get(candidate_name=mycos, candidate_position=mypos)
    cos.candidate_votes += 1
    cos.save()
    username = request.user.username
    vos = Votes.objects.create(voter_id=username, position=mypos)
    vos.save()
    return redirect("vote")


def home(request):
    if request.POST:
        form = CaptchaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + "?ok")
    else:
        form = CaptchaForm()

    return render(request, "home.html", {"form": form})
# Create your views here.

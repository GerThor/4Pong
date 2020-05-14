from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse

from . import models
from . import forms

import json 

# Create your views here.

@login_required
def homePage(request):
  context = {
    "title": "HomePage",
    "header": "About 4Pong"
    
  }
  
  username = request.user.username
  print("Hello")
  print(username)
  return render(request, "homePage.html", context=context)

@login_required
def leaderBoard(request):

  gamesWon = models.gameModel.objects.order_by('-gamesWon')[:20]
  
  context = {
    "title": "LeaderBoard",
    "header": "LeaderBoards",
    "wins": gamesWon,

    
  }
  return render(request, "leaderBoard.html", context=context)

@login_required
def gameLobby(request):
  context = {
    "title": "GameLobby",
    "header": "Game Lobby"
    
  }
  if request.method == "POST":
    query = models.gameModel.objects.get(author=request.user)
    query.gamesWon += 1
    query.save()
  return render(request, "gameLobby.html", context=context)


#Registration view adapted from class examples
def register(request):
  if request.method == "POST":
      form_instance = forms.RegistrationForm(request.POST)
      if form_instance.is_valid():
          user = form_instance.save()
          form = forms.gameForm(request.POST)
          form.save(user)
          return redirect("/login/")
  else:
      form_instance = forms.RegistrationForm()
  context = {
      "form":form_instance,
  }
  return render(request, "registration/register.html", context=context)

def logout_view(request):
  logout(request)
  return redirect("/login/")

def getWins(request):
  gamesWonObjects = models.gameModel.objects.order_by('-gamesWon')[:20]
  gamesWonList = {}
  gamesWonList["wins"] = []
  for i in gamesWonObjects:
    tempWins = {}
    tempWins["gamesWon"] = i.gamesWon
    tempWins["author"] = i.author.username
    gamesWonList["wins"] += [tempWins]

  return JsonResponse(gamesWonList)

#Chat stuff
@login_required
def chatPage(request):
  return render(request, 'chat/chatPage.html', {})

@login_required
def room(request, room_name):
  return render(request, 'chat/room.html', {
    'room_name': room_name,
  })
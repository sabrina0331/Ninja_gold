from django.shortcuts import render,HttpResponse,redirect
import random

def index(request):
    return render(request,"ninja_gold/index.html")

def process_money(request):
    if not 'activity' in request.session:
        request.session['activity'] = []
    if not 'total_gold' in request.session:
        request.session['total_gold'] = 0

    places = request.POST['places']
    if places == 'farm':
        money = random.randint(10,20)
    elif places == 'cave':
        money = random.randint(5,10)
    elif places == 'house':
        money = random.randint(2,5)
    elif places == 'casino':
        money = random.randint(-50,50)
    if money > 0:
        message = "Earned {} from {}".format(money,places) 
    else:
        message = "Lost {} golds in a casino, please save your money".format(money)

    activity = {'message': message}

    request.session['activity'].append(activity)
    request.session['total_gold'] += money 

    print("earned/lost " + str(money) +" from "+places +", now your total gold is "+str(request.session['total_gold']))

    return redirect("/")

def playAgain(request):
    request.session['activity'] = []
    request.session['total_gold'] = 0
    return redirect("/")

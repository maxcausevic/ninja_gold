from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = ""
    return render(request, 'index.html')
def process_money(request):
    if 'activity_log' not in request.session:
        request.session["activity_log"] = []
    if request.POST["location"] == "farm":
        gold = random.randint(10,20) 
        request.session["gold"]+= gold
        request.session['activity_log'].append("Went to the farm")
        print(f"Earned {gold}")
    if request.POST['location'] == "cave":
        gold = random.randint(5,10)
        request.session["gold"]+= gold
        request.session['activity_log'].append("Went to the cave")  
        print(f"Earned{gold}")
    if request.POST['location'] == 'house':
        gold = random.randint(2,5)
        request.session["gold"]+= gold
        request.session['activity_log'].append("Went to the house")
        print(f"Earned{gold}")
    if request.POST['location'] == 'casino':
        gold = random.randint(-50,50)
        request.session["gold"]+= gold
        request.session['activity_log'].append("Went to the casino")
        print(f"Earned {gold}")
    
    return redirect("/")

def destroy(request):
    del request.session['gold']
    return redirect('/')
        



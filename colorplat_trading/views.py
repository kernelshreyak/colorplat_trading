from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from colorplat_trading.models import *

def index(request):
    plats = ColorPlat.objects.all()
    return render(request, 'index.html', {'plats': plats})

# Show prices on home page. This is called via AJAX
def showpriceshome(request):
    plats = ColorPlat.objects.all()

    resp = ""

    for plat in plats:
        resp += """
            <div class="plat">
            {name}<br/>
            {currentprice}<br/>
            <div style="width:20px;height:20px;background-color: rgb({rvalue}, {gvalue}, {bvalue});"></div>
            </div>
        """.format(name=plat.name,currentprice=plat.currentprice(),rvalue=plat.rvalue,gvalue=plat.gvalue,bvalue=plat.bvalue)

    return HttpResponse(resp)

# Show all trades of current user
def showtrades(request):
    pass

# Create a new trade
def addtrade(request):
    trade = Trade()
    trade.platsamount = 0
    trade.amount = 0

    trade.save()

    return redirect("/")
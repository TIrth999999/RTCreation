# MODEL IMPORT
from app.models import *
from django.shortcuts import render, redirect

def index(request):
    
    counter, created = VisitorCounter.objects.get_or_create(id=1)
    
    if request.method == "POST":
        counter.count += 1
        counter.save()
        return redirect("home")

    if not request.session.get('has_visited'):
        counter.count += 1
        counter.save()
        request.session['has_visited'] = True

    reviews = Reviews.objects.all()

    return render(request,'index.html',{'counter': counter,'reviews': reviews})

def review(request):

    reviews = Reviews.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        rating = request.POST.get('rating')
        review = Reviews(name=name, email=email, desc=desc, rating=rating)
        review.save()

    return render(request,'review.html',{'reviews': reviews})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = request.POST.get('contact')
        contactObj = Contact(name=name, email=email, desc=desc, contact=contact)
        contactObj.save()

    return render(request,'contact.html')
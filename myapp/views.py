from django.shortcuts import render, HttpResponse, redirect
from . models import Member, Course, Contact
# Create your views here.

def home(request):
    # return HttpResponse("This is home page")
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def courses(request):
    allCourse = Course.objects.all()
    return render(request, 'courses.html', {'allCourse':allCourse})
def coursedetails(request, slug):
    fullDetails = Course.objects.filter(slug=slug).first()
    return render(request, 'coursedetails.html', {'fullDetails':fullDetails})
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        course = request.POST['course']
        empdetails = Contact(name=name, email=email, contact=contact, course=course)
        empdetails.save()
        return redirect("/")
    return render(request, 'contact.html')

def members(request):
    all_members = Member.objects.all()
    return render(request, 'members.html', {'all': all_members})

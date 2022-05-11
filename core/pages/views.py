from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def aboutus(request):
    return  render(request,'pages/aboutus.html')

def patner(request):
    return  render(request,'pages/ourpatners.html')

def contactus(request):
    return render(request, 'pages/contactus.html')

def demo(request):
    return  render(request,'pages/demo.html')


# form on demo.html 
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'demo.html', {'form': form})


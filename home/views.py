from django.shortcuts import render

# Create your views here.

def home_page(request):
    context = {
        'title' : 'Hello World',
        'content' : 'Welcome to the homepage',
    }

    # @TODO: if user.is_authenticated

    return render(request, 'home_page.html', context)


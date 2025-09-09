from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title': 'The Kitman\'s Shop',
        'npm' : '2406403381',
        'name': 'Rayhan Derya Maheswara',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
from django.shortcuts import render
# feedpage/view.py
...
def index(request):
    return render(request, 'feedpage/index.html')
    
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'levu/index.html')

def add_expense(request):
    return render(request, 'levu/add_expense.html')
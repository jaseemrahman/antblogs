from datetime import datetime
from django.shortcuts import render
from datetime import datetime
# Create your views here.

def home(request):
    dict_date={
        "today":datetime.today()
    }
    return render(request,'home.html',dict_date)

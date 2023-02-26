from django.shortcuts import render
from SBData.models import Detail
from django.shortcuts import render, get_object_or_404
def index(request):
    #fetching form data
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        weight = request.POST['weight']

        # storing data to the database
        ins = Detail(name=name, age=age,weight=weight)
        ins.save()
        return render(request, 'show.html', {'ins': ins})
    else:
        return render(request, 'form.html')
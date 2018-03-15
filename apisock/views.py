from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def api(request):
    context = {}
    if request.method == "POST":
        for key in request.POST:
            context[key] = request.POST[key]
    print(context)
    return render(request,'apisock/home.html',{'context':context})

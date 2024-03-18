from django.http import HttpResponse

# from django.shortcuts import render

def note(request):
    return HttpResponse(b'Hello from Notes app.')
    # return render(
    #     request=request,
    # )
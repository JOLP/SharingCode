from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.


def register_success(request):
    return render_to_response(
    'homepage.html',
    )



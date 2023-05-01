from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import UserDetails
# Create your views here.

@api_view(['POST'])
def login(request):
    mobile = request.data.get("mobile", "")
    password = request.data.get("password", "")

    user = UserDetails.objects.filter(mobile=mobile).first()

    if(not user):
        return Response(status=401)
    if(user.password == password):
        return Response(status=102)
    return Response(status=401)

    return render(request, 'index.html')

def register(request):
    pass
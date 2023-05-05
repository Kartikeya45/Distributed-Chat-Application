from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import UserDetails
# Create your views here.

@api_view(['POST'])
def login(request):
    print(request.data)
    phone = request.data.get("phone", "")
    password = request.data.get("password", "")

    user = UserDetails.objects.filter(phone=phone).first()

    if(not user):
        print("first")
        return Response(status=401)
    if(user.password == password):
        # Success condition

        return Response(user.name ,status=200)
    
    return Response(status=401)

    return render(request, 'index.html')

@api_view(['POST'])
def register(request):
    print(request.data)
    name = request.data.get("name", "")
    password = request.data.get("password", "")
    phone = request.data.get("phone", "")

    user = UserDetails(
        name=name,
        phone=phone,
        password=password
    )
    user.save()
    return Response(status=200)
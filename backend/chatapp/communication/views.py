from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MessageSerializer

from .models import *

# Create your views here.

@api_view(['POST', 'GET'])
def chat(request):
    print("<<<<<<<<<<<<<<<<<")
    print(request.method)
    print("<<<<<<<<<<<<<<<<<")
    accessor = request.data["accessor"]
    accessed = request.data["accessed"]

    if(request.method == 'GET'):  
        print(accessed)  
        if(accessed["group"] == False):
            user = Message.objects.filter(key=min(accessor["name"], accessed["name"]) + max(accessor["name"], accessed["name"]))
            print(user)

            all_messages = []
            for i in user:
                all_messages.append(MessageSerializer(i).data)
            return Response(all_messages)
        else:
            pass

    if(request.method == 'POST'):
        # if(accessed<accessor):

        msg = Message(
            sender=accessor["name"],
            receiver=accessed["name"],
            key=min(accessor["name"], accessed["name"]) + max(accessor["name"], accessed["name"]),
            body=request.data["body"],
            group=False
        )
        msg.save()

        return Response(status=200)


    mobile = request.data.get("mobile", "")
    password = request.data.get("password", "")

    user = UserDetails.objects.filter(mobile=mobile).first()

    if(not user):
        return Response(status=101)
    if(user.password == password):
        return Response(status=102)
    return Response(status=103)

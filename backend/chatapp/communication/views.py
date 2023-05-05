from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MessageSerializer

from .models import *

# Create your views here.

@api_view(['POST', 'GET'])
def chat(request):
    print("<<<<<<<<<<<<<<<<<")
    # print(request.GET["accessed"])
    # print(request.GET["accessor"])
    print("<<<<<<<<<<<<<<<<<")
    # accessor = request.data["accessor"]
    # accessed = request.data["accessed"]

    if(request.method == 'GET'):  
        print(request.GET['accessor'])  
        print(request.GET['accessed'])  
        if(request.GET['group'] == 'false'):
            user = Message.objects.filter(key=min(request.GET['accessor'], request.GET['accessed']) + max(request.GET['accessor'], request.GET['accessed']))
            print(user)

            all_messages = []
            for i in user:
                all_messages.append(MessageSerializer(i).data)
            return Response(all_messages)
        else:
            pass

    if(request.method == 'POST'):
        # if(accessed<accessor):
        accessor = request.data["accessor"]
        accessed = request.data["accessed"]

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

@api_view(['POST', 'GET'])
def contacts(request):
    current_user = request.data['user']

    for_sender = Message.objects.filter(sender=current_user).values()
    for_recv = Message.objects.filter(receiver=current_user).values()

    unique_contacts = []
    unique_names = []
    
    for person in for_sender:
        if(person['receiver'] not in unique_names):
            send_name = UserDetails.objects.get(phone=person['receiver'])
            print(send_name.name, type(send_name))
            unique_contacts.append({
                "name": send_name.name,
                "phone": person['receiver']
            })
            unique_names.append(person['receiver'])
    
    for person in for_recv:
        if(person['sender'] not in unique_names):
            send_name = UserDetails.objects.get(phone=person['sender'])
            
            unique_contacts.append({
                "name": send_name.name,
                "phone": person['sender']
            })
            unique_names.append(person['sender'])
    
    print(unique_contacts)
    
    return Response(unique_contacts)
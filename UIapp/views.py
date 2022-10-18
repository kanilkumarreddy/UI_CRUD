from django.shortcuts import render
from . models import Bank_Customer
from django.http import HttpResponse
from django.template import RequestContext
from rest_framework.decorators import api_view
from django.shortcuts import redirect
# 
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from . serializers import CustomerSerializer



def list(request):
    showall=Bank_Customer.objects.all()
    return render(request,"index.html",{"data":showall})

def get(request,id):
    customer=Bank_Customer.objects.get(id=id)
    details=Bank_Customer.objects.all()
    context= {
        'customer':customer,
        'details':details
    }
    return render(request,"get.html",context)

def insert(request):
    saverecord=Bank_Customer()
    f=saverecord.choice
    return render(request,'insert.html',{'choice':f})

def insert1(request):
    if request.method=="POST":
        saverecord=Bank_Customer()
        saverecord.id=request.POST.get('id')
        saverecord.Name=request.POST.get('Name')
        saverecord.Account_Number=request.POST.get('Account_Number')
        saverecord.IFSC_code=request.POST.get('IFSC_code')
        saverecord.Branch=request.POST.get('Branch')
        saverecord.Mobile_NO=request.POST.get('Mobile_NO')
        saverecord.Email_id=request.POST.get('Email_id')
        saverecord.Address=request.POST.get('Address')
        saverecord.save()
        return render(request,'insert.html',{"result":"Customer " +saverecord.Name+  " added successfully"})  
    else:
        return render(request,'insert.html')

def edit(request,id):
    customer=Bank_Customer.objects.get(id=id)
    details=Bank_Customer.objects.all()
    context= {
        'customer':customer,
        'details':details
    }
    return render(request,"update.html",context)

def update(request,id):
    saverecord=Bank_Customer.objects.get(id=id)
    saverecord.id=request.POST.get('id')
    saverecord.Name=request.POST.get('Name')
    saverecord.Account_Number=request.POST.get('Account_Number')
    saverecord.IFSC_code=request.POST.get('IFSC_code')
    saverecord.Branch=request.POST.get('Branch')
    saverecord.Mobile_NO=request.POST.get('Mobile_NO')
    saverecord.Email_id=request.POST.get('Email_id')
    saverecord.Address=request.POST.get('Address')
    saverecord.save()
    return render(request,'insert.html',{"result":"Customer " +saverecord.Name+  " updated successfully"})  

def delete(request,id):
    customer=Bank_Customer.objects.get(id=id)
    customer.delete()
    return redirect("list")


# Api

@api_view(['GET'])
def list1(request):
    products=Bank_Customer.objects.all()
    serializers=CustomerSerializer(products,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get1(request,id):
    customer=Bank_Customer.objects.get(id=id)
    serializer=CustomerSerializer(customer,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create1(request):
    serializer=CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def update1(request,id):
    product=Bank_Customer.objects.get(id=id)
    serializer=CustomerSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete1(request,id):
    product=Bank_Customer.objects.get(id=id)
    product.delete()
    return Response("Product successfully deleted")

class Customerview(viewsets.ModelViewSet):
    queryset=Bank_Customer.objects.all()
    serializer_class=CustomerSerializer
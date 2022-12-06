from logging import exception
from multiprocessing import managers
from xmlrpc.client import ResponseError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer
from .models import *

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(['POST'])
 
def teacher_auth(request):
    
     
    params=request.data
    statusCode=0
    email=params['email']
    passwd=params['passwd']
    
    try:
        login_check=Teacher.objects.get(email=email,password=passwd)
        statusCode=200
    except:
        statusCode=401
        return Response({'statusCode':statusCode})
    return Response({'statusCode':statusCode})

@api_view(['GET'])
def view_teachers(request):
    
    teachers=Teacher.objects.all()
    ser=TeacherSerializer(teachers,many=True)
    return Response(ser.data)

@api_view(['POST'])
def add_student(request):
    params=request.data
    statusCode=0

    s_name = params['s_name'] 
    s_email = params['s_email'] 
    s_gender = params['s_gender'] 
    s_phone = params['s_phone'] 
    s_address = params['s_address']
    s_username = params['s_username']  
    s_passwd = params['s_passwd'] 

    try:
        exist =Student.objects.filter(s_email = s_email).exists()

        if not exist :


            student = StudentSerializer(data = params)

            if student.is_valid():

                student.save()

                statusCode= 200
        else : 
            statusCode = 409

    except Exception as e:
        print(e)

        statusCode=401  
    
    return Response({'statusCode':statusCode})

@api_view(['GET'])
def load_students(request):
    
    students=Student.objects.all()
    ser=StudentSerializer(students,many=True)
    return Response(ser.data)

@api_view(['DELETE'])
def delete_student(request,id):
     
    statusCode= 0 
     

    try:
        student = Student.objects.get(id = id)
        student.delete()
        statusCode = 200
    
    except:
        statusCode = 409
        pass

    return Response({'statusCode':statusCode})


@api_view(['PUT'])
def update_student(request,id):
    # params=request.data
    statusCode=0

    try:
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            statusCode = 200
        else:
            pass

    except Exception as e:
        print(e)
        statusCode = 409
        pass

    return Response({'statusCode':statusCode})



@api_view(['GET'])
def loadSingleStudent(request,id):
    statusCode = 0
    try:
        student = Student.objects.get(id = id)
 
        ser=StudentSerializer(student)
        return Response(ser.data)
    except Exception as e:
        print(e)
        statusCode = 404
        
        return Response({'statusCode':statusCode})
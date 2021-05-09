from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Advisor,User,Booking
from .serializers import AdvisorSerializer,UserSerializer,BookingSerializer
''' A module to make a endponits.
...
Attributes
----------
get:
to return required data
post:
to create he required the data
'''

class AdvisorApi(APIView):
    parser_classes = (MultiPartParser,FormParser)
    def post(self,request,format = None):
        serializer = AdvisorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data created"},status = status.HTTP_200_OK)
        return Response(serializer.errors,\
        status = status.HTTP_400_BAD_REQUEST)

class UserApi(APIView):
    def post(self,request,format = None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        stu = User.objects.get(email = request.data['email'])
        serializer = UserSerializer(stu)
        new_user = dict(serializer.data)
        id_new = new_user['id']
        tokens = str(RefreshToken.for_user(stu))
        return Response({"User_id":id_new ,"JWT_Token":tokens},\
        status = status.HTTP_200_OK)

class UserLogin(APIView):
    def post(self,request,format = None):
        email = request.data['email']
        password =request.data['password']
        
        if email is None or password is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        try: 
            Use = User.objects.get(email = email)
        except :
            return Response({"msg":"incorrect email or password"},\
            status = status.HTTP_401_UNAUTHORIZED)
        if Use:
            serializer = UserSerializer(Use)
            register_user = dict(serializer.data)
            registered_pass = register_user['password']
            if password == registered_pass:
                tokens = str(RefreshToken.for_user(Use))
                id_new = register_user['id']
                return Response({"user_id": id_new,"JWT_Token": tokens},\
                status = status.HTTP_200_OK)
            
            return Response(status = status.HTTP_401_AUTHENTICATION_ERROR)
        else:
            return Response(satuts = status.HTTP_401_AUTHENTICATION_ERROR)


class AdvisorList(APIView):
    def get(self , request , pk ,format = None):
        id_reg = pk
        if id_reg :
            try:
                use = User.objects.get(id = id_reg)
            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        if use:
            advisor = Advisor.objects.all()
            serializer = AdvisorSerializer(advisor,many = True)
            return Response(serializer.data)

class Bookings(APIView):
    def post(self,request,pk,fk):
        user_id = pk
        advisor_id = fk
        try:
            user = User.objects.get(id = user_id)
            advisor = Advisor.objects.get(id = advisor_id)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        serializer1 = UserSerializer(user)
        user_dict = dict(serializer1.data)
        serializer2 = AdvisorSerializer(advisor)
        advisor_dict = dict(serializer2.data)
        username,id_user = user_dict['username'],user_dict['id']
        advisorname,id_advisor = advisor_dict['advisorname'],advisor_dict['id']
        date = request.data['date']
        Booking.objects.create(username = username,userid = id_user,\
        advisorname = advisorname,advisorid = id_advisor,time =date)
        return Response(status = status.HTTP_200_OK)

class SeeBookings(APIView):
    def get(self,request,pk,format = None):
        id_reg = pk
        try:
            use = User.objects.get(id = id_reg)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if use:
            book = Booking.objects.get(userid = id_reg)
            serializer= BookingSerializer(book)
            bookingDetails = dict(serializer.data)
            advisor_id = bookingDetails['advisorid']
            advisor_obj = Advisor.objects.get(id = advisor_id)
            serializer_advisor = AdvisorSerializer(advisor_obj)
            advisor_dict = dict(serializer_advisor.data)
            pic = advisor_dict['picture']
            return Response({"advisorname": bookingDetails['advisorname'],'advisor_profilePic':pic,\
            'advisorid':bookingDetails['advisorid'],\
            'bookingid': bookingDetails['id'],'time':bookingDetails['time']})

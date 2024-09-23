from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .serializers import RegistrationSerializer, LoginSerializer,UserSerializer
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from .models import CustomUser
from django.utils.encoding import force_bytes
from rest_framework import status

# class UserRegistrationAPIView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))

#             confirm_link = f"http://127.0.0.1:8000/api/users/activate/{uid}/{token}/"
#             email_subject = "Confirm Your Email"
#             email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
#             email = EmailMultiAlternatives(email_subject, '', to=[user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()
#             return Response({"detail": "Check your mail for confirmation"})
#         return Response(serializer.errors)

class UserRegistrationAPIView(APIView):
    serializer_class=RegistrationSerializer


    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            print(user)
            token=default_token_generator.make_token(user)
            print("token",token)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print("uid",uid)
            confirm_link = f"https://onlineschool-im71.onrender.com/api/users/activate/{uid}/{token}/"
            email_subject="Confirm Your Email"
            # Choose the email template based on user type
            if user.user_type == 'teacher':
                email_template = 'confirm_teacher_email.html'
            else:
                email_template = 'confirm_student_email.html'

            email_body = render_to_string(email_template, {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({"detail": "Check your email for confirmation"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = CustomUser.objects.get(pk=uid)
    except (CustomUser.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('https://onlinescl.netlify.app/login.html')
    else:
        return redirect('register')

class UserLoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'key': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLoginApiView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data = self.request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']

#             user = authenticate(username= username, password=password)
            
#             if user:
#                 token, _ = Token.objects.get_or_create(user=user)
#                 print(token)
#                 print(_)
#                 login(request, user)
#                 return Response({'token' : token.key, 'user_id' : user.id})
#             else:
#                 return Response({'error' : "Invalid Credential"})
#         return Response(serializer.errors)

    
# fdfdhgf

class UserLogoutAPIView(APIView):
    def get(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            pass
        logout(request)
        return Response({"detail": "Logged out successfully."})



class UserListAPIView(APIView):

    def get(self, request):
        # users = CustomUser.objects.all()
        users = CustomUser.objects.filter(user_type='teacher')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
from rest_framework.generics import RetrieveAPIView
class UserDetailAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
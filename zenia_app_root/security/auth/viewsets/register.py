import django.contrib
import random; 
from datetime import timedelta
from zenia_app_root.security import base_url
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import random
from django.conf import settings
from django.template.loader import render_to_string
import string
from django.views import View
from rest_framework.response import Response
import resend
from zenia_app_root.security.auth.utils import generate_token
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError,force_str
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from zenia_app_root.security.auth.serializer.register import RegisterSerializer
# from email_msg_generator.models import OpenAiAdminModel,OpenAiUserModel
# from services.aichat.models im# The commented out lines in the code are likely imports that are not
# currently being used in the codebase. These lines are usually kept
# as comments for reference or in case they need to be re-enabled in
# the future.
from zenia_app_root.security.user.models import User
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
# from core.wallet.models import UsdModel
from zenia_app_root.security.auth.serializer.verify_serializer import VerifySerializer
from rest_framework import status
from zenia_app_root.security.auth.models import CodeGenerator
from django.core.mail import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
import requests
@swagger_auto_schema(
    request_body=RegisterSerializer,
    responses={200: RegisterSerializer}
)


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def generate_random_link(self,length=20):
        # Define the characters allowed in the link
        characters = string.ascii_letters + string.digits

        # Generate a random link by selecting characters randomly
        random_link = ''.join(random.choice(characters) for _ in range(length))

        return random_link
    
    def create(self, request, *args, **kwargs):
        try:
            print(request.data)
            serializer = self.serializer_class(data=request.data)
            email=str(serializer.initial_data['email'])
            email_user=email
            username=str(serializer.initial_data['username'])
            # print(serializer.initial_data['password'])
            password_length=int(len(serializer.initial_data['password']))
            print(password_length)
            print(type(password_length))
            error_list=[]
            if not serializer.is_valid():
                print("not valid")
                if User.objects.filter(email=email).exists():
                    # return Response({'message':'User with this email already exists','error':True,'field':'email'},status=status.HTTP_403_FORBIDDEN)
                    email_error='User with this email already exists'
                    error_list.append(email_error)
                if password_length<8:
                    # print(password_length)
                    # print(type(password_length))
                    password_error='Password should be at least 8 characters'
                    error_list.append(password_error)
                
                if User.objects.filter(username=username).exists():
                    username_error='username exist'
                    error_list.append(username_error)
                if str(serializer.initial_data['confirm_password'])is not str(serializer.initial_data['password']):
                    password_mismatch_error='Password mismatch for confirm password'
                
                    error_list.append(password_mismatch_error)
                
                error_list=error_list
                return Response({'error_message':error_list[0],'status':False},status=status.HTTP_406_NOT_ACCEPTABLE)
            # if serializer.is_valid():
            else:
                

                print("validated good")
                

                
                # unassigned_keys=OpenAiAdminModel.objects.filter(assigned=False).first()

                # if unassigned_keys:
                #     unassigned_keys.assigned=True

                #     open_api_key=unassigned_keys.open_ai_key

                #     unassigned_keys.save()

                #     OpenAiUserModel.objects.create(user=user,custom_user_key_id=unassigned_keys.custom_user_key_id,open_ai_key=open_api_key,time_of_assiging=timezone.now())
                # User.objects.get(email=request.user.email).is_active=False
                # import resend
                # resend.api_key = "re_QPQ9uUgC_AQgi1DuGsDWDMTxxUyo88XPi"
                # from core_app_root.security.base_url import main_url
                # from core_app_root.security import base_url
                # full_url=main_url+self.generate_random_link()
                
                # r = resend.Emails.send({
                # "from": "send@christiankelechieze.com",
                # "to": f"{email}",
                # "subject": "Account Verification",
                # "html": f"""<p>Congrats on Signing up <strong> with Codeblaze Academy</strong> click this link <a href="{base_url.main_url}account/verify/{email}/">{self.generate_random_link()}</a> to verify your account </p>"""
                # })
                import random
                activation_code=random.randint(1000, 9999)
                # import smtplib
                # from email.mime.multipart import MIMEMultipart
                # from email.mime.text import MIMEText
            
                # # Define the email details
                
                message = f"""
                Dear {serializer.validated_data['username']},
    Congratulations on signing up for Xpresscad, the revolutionary AI-powered CAD modeling tool We're thrilled to have you on board and can't wait for you to experience all that Xpresscad has to offer.
    Xpresscad is more than just a typical CAD software - it's a cutting-edge tool that uses voice feedback to guide you through the creation and modification of 3D models. With Xpresscad, you'll enjoy the following incredible features:
    Real-Time Voice Feedback
    Xpresscad's AI-powered algorithms provide real-time audio feedback, guiding you through the creation and modification of 3D models. This ensures that your designs are accurate and precise.
    Advanced Shape Creation and Modification
    Create basic geometric shapes like spheres, cubes, rectangular boxes, and cones. Perform advanced modifications such as cutting holes, changing hole shapes, creating chamfers, rounding edges, and shelling out material. Xpresscad's AI provides feedback similar to PTC Creo’s features, facilitating a seamless and intuitive design process.
    User-Friendly Interface
    Xpresscad offers a user-friendly interface that supports voice commands for all operations. This makes it easy to create and modify 3D models without the need for complex keyboard and mouse commands.
    High Precision and Accuracy
    Xpresscad ensures high precision and accuracy in model creation and modifications, helping you achieve the exact designs you envision.
    We're confident that Xpresscad will revolutionize your CAD experience and help you create stunning 3D designs. Get ready to experience the future of CAD modeling!
    If you have any questions or need assistance getting started, please don't hesitate to reach out to our friendly support team. We're here to help you every step of the way.
    Welcome to the Xpresscad family - let's get designing!
    Best regards,
    Codeblaze Xpress
    Xpresscad Corporation
                
                """
                                    
                receiver_email = email
                subject = "Account Activation Code"
                # body = f"Enter the four digit code sent to you here in your Blanc Exchange application to continue with account registration completion   {activation_code} , you can copy and paste the activation code"
                mail_body={
                    "userEmail":receiver_email,
                    "text":message,
                    "subject":"New User Registration",
                    "title":f"Account Created Successfully"
                }
                
                response_mail=requests.post(url="https://zenia-email-api.vercel.app/api/v1/register_email",json=mail_body)
                
                if str(response_mail.json()['msg'])=="You should receive an email from us":
                    
                    user=serializer.save()
                    # user.is_active=False
                    user.is_confirmed=True
                    user.save()
                
                    
                
                    serializer_data = serializer.data.copy()  # Create a copy of the serializer data
                    serializer_data.pop('confirm_password', None) 
                    
                    return Response({
                        "user": serializer_data,
                        "status":True,
                        "detail":"Account creation successful, check email to get your authentication code"
                    }, status=status.HTTP_201_CREATED)   
                
            
                return Response({
                        "user": serializer_data,
                        "status":True,
                        "detail":"Account creation successful, check email to get your authentication code"
                }, status=status.HTTP_201_CREATED)   
        
        except:
            return Response({
                    
                        "status":False,
                        "detail":"Network error ,try again later"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    # return Response({'error': 'No unassigned keys available.'}, status=status.HTTP_404_NOT_FOUND)
    # else:
    #     return Response({"error":"User with this Api have an existing api key"},status=status.HTTP_403_FORBIDDEN)

class ActivateAccountView(viewsets.ModelViewSet):
    serializer_class = VerifySerializer
    permission_classes=[IsAuthenticated,]
    queryset=User.objects.all()
    http_method_names=['post']
    # @action(detail=False, url_path='verify/(?P<email>[^/]+)')
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        
        
        if serializer.is_valid():
            try:
                code_authentication=serializer.validated_data['code_authentication']
                user = User.objects.get(email=request.user.email)

                current_user=CodeGenerator.objects.get(user__email=request.user.email)
                activation_code=current_user.code_authentication
                
                if user.is_confirmed==True:
                    return Response({"status":False,"detail":"You have already verified your account"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    
                    if str(code_authentication)==str(activation_code):
            
                        user.is_confirmed=True
                        user.save()
                        
                        
                        return Response({"status":True,"detail":f"Acount verified successfully for {request.user.email}"},status=status.HTTP_200_OK)
                    else:
                        
                    
                    
                        return Response({"status":True,"detail":f"Acount cannot  not be verified due to incorrect code {request.user.email}"},status=status.HTTP_406_NOT_ACCEPTABLE)
                
            except:
                return Response({"detail":"Your request cant be processed now, check your network and try again"})
            
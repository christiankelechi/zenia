from zenia_app_root.geometries_management.serializers.prompt_serializer import MessagePrompt
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework import status 
from zenia_app_root.geometries_management.viewsets import base_url
import requests
from rest_framework.permissions import AllowAny
from zenia_app_root.geometries_management.serializers.chair import ChairSerializer
class MessagePromptViewset(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    http_method_names=['post']
    serializer_class=MessagePrompt
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                print(serializer.data)
                if 'chair' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}complexshapes/chair/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                elif 'gear' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}complexshapes/gear/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                elif 'hammer' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}complexshapes/hammer/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                elif (('feeder' in str(serializer.validated_data['message_body'])) and ('hole' in str(serializer.validated_data['message_body']))):
                    response=requests.get(f"{base_url.url}edit/hollow/complexshapes/feeder/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                elif 'feeder' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}complexshapes/feeder/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                elif 'cuboid' in str(serializer.validated_data['message_body']) and ('hole' in str(serializer.validated_data['message_body'])):
                    response=requests.get(f"{base_url.url}edit/hollow/complexshapes/cuboid/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                elif 'cuboid' in str(serializer.validated_data['message_body']) and not ('hole' in str(serializer.validated_data['message_body'])):
                    response=requests.get(f"{base_url.url}complexshapes/cuboid/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                elif 'savingbox' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}complexshapes/savingbox/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                elif 'bottle' in str(serializer.validated_data['message_body']) and not 'hole' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}complexshapes/bottle/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                elif 'beam' in str(serializer.validated_data['message_body']) and not 'hole' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}complexshapes/beam/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                elif 'bottle' in str(serializer.validated_data['message_body']) and 'hole' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}edit/holow/complexshapes/bottle/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                elif 'feeder' in str(serializer.validated_data['message_body']) and  'hole' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}edit/hollow/complexshapes/feeder/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                
                elif 'cube' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}basicshapes/cube/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                elif 'sphere' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}basicshapes/sphere/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                
                elif 'cone' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}basicshapes/cone/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                elif 'cuboid' in str(serializer.validated_data['message_body']):
                    response=requests.get(f"{base_url.url}basicshapes/cuboid/")
                    
                    response=response.json()
                    
                    return Response({"status":True,"message":"Your desired shape created successfully",'data':response},status=status.HTTP_200_OK)
                else:
            
                    
                    return Response({"status":False,"message":"Your desired shape created successfully",'data':{"stl_url":None,"status":False,"message":"Assets not found"}},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status":False,"message":f"{e}Internal server error , check your network and try again",'data':{"stl_url":None,}},status=status.HTTP_404_NOT_FOUND)
            
            
        return Response({"status":True,"message":"Your desired shape created successfully"},status=status.HTTP_200_OK)
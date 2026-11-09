from rest_framework import routers
from zenia_app_root.voice_recognition.viewsets import voice_recognition

router=routers.SimpleRouter()
router.register(r'voice/record',voice_recognition.VoiceRecognitionViewset,basename='voice_prompt')


urlpatterns=[
    *router.urls
]


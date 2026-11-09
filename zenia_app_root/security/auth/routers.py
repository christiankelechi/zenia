from rest_framework import routers
from zenia_app_root.security.auth.viewsets.register import RegisterViewSet,ActivateAccountView
from zenia_app_root.security.auth.viewsets.login import LoginViewSet
from zenia_app_root.security.auth.viewsets.promptmessage import MessagePromptViewset
router=routers.SimpleRouter()
router.register(r'register',RegisterViewSet,basename='register')
router.register(r'login',LoginViewSet,basename='login'),




urlpatterns=[
    *router.urls
]

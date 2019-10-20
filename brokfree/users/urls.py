from django.conf.urls import url
from users.views import signup,prof,manual,log_out

urlpatterns = [
    url(r'signup/$',signup),
    url(r'profile/$',prof),
    url(r'login/$',manual),
    url(r'login/profile/$',prof),
    url(r'signup/profile/$',prof),
    url(r'logout/$',log_out),
]

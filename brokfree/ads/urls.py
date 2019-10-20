from django.conf.urls import url
from ads.views import enter_vals,post_ad,search,viewhome,post,filtered
urlpatterns = [
    #url(r'createhome/',enter_vals),
    url(r'post/$', post_ad),
    url(r'^search/$', search),
    url(r'^prop/([1-9][0-9]{0,2})/$',viewhome),
    #url(r'check/$',check),
    url(r'posted/$',post),
    url(r'filter/$',filtered),
]

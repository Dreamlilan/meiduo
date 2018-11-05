from django.conf.urls import url

from verifications import views

urlpatterns = [
url(r'^imagecodes/(?P<image_code_id>.+)/$',views.RegisterImageCodeView.as_view(),name='imagecode'),
]








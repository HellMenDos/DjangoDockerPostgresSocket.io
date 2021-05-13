from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/get/more/', views.MoreData.as_view(),name='moreData'),
    path('social/auth/google/<str:token>', views.GetDataFromGoogle.as_view(),name='google'),
    path('social/auth/vk/<str:token>', views.GetDataFromVk.as_view(),name='vk'),
    path('social/auth/appleid/<str:token>', views.GetDataFromApple.as_view(),name='appleid'),
    path('social/auth/facebook/<str:token>', views.GetDataFromFacebook.as_view(),name='facebook'),
    path('auth/get/more/one/<int:num>', views.OneUserData.as_view(),name='getOne'),
    path('auth/activate/<str:uid>/<str:token>/', views.activate,name='activate'),
    path('auth/change/group/<str:name>/<int:userId>', views.ChangeGroup.as_view(),name='changeGroup'),
    path('auth/change/password/sms/', views.ChangePassword.as_view(),name='sms'),
    path('support/', views.SupportConf.as_view(),name='support'),
    path('push/', views.PushConf.as_view(),name='push'),
    path('general/', views.GeneralConf.as_view(),name='general'),
]


 
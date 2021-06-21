from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/get/more/', views.MoreData.as_view(), name='moreData'),
    path('auth/tokin/login/number/',
         views.LoginWithNumber.as_view(), name='moreData'),
    path('auth/update/more/', views.MoreDataUpdate.as_view(), name='moreDataUpdate'),
    path('auth/update/more/photo/',
         views.MoreDataUpdatePhoto.as_view(), name='moreDataUpdate'),
    path('social/auth/google/', views.GetDataFromGoogle.as_view(), name='google'),
    path('social/auth/vk/', views.GetDataFromVk.as_view(), name='vk'),
    path('social/auth/appleid/', views.GetDataFromAppleId.as_view(), name='appleid'),
    path('social/auth/facebook/',
         views.GetDataFromFacebook.as_view(), name='facebook'),
    path('auth/get/more/one/<int:num>',
         views.OneUserData.as_view(), name='OneUserData'),
    path('activate/<str:uid>/<str:token>/', views.activate, name='activate'),
    path('auth/change/group/<str:name>/<int:userId>',
         views.ChangeGroup.as_view(), name='changeGroup'),
    path('auth/get/company/<str:name>/<str:username>/<str:location>',
         views.GetCompanyWithLocation.as_view(), name='GetCompanyWithLocation'),
    path('auth/get/company/<str:name>/<str:username>/',
         views.GetCompany.as_view(), name='GetCompany'),
    path('auth/get/location/<str:name>/<int:location>/',
         views.GetCompanyLocationId.as_view(), name='GetCompanyLocationId'),
    path('auth/get/company/<str:name>/',
         views.GetAllCompanys.as_view(), name='GetAllCompanys'),
    path('auth/change/password/sms/',
         views.ChangePassword.as_view(), name='ChangePassword'),
    path('support/', views.SupportConf.as_view(), name='support'),
    path('push/', views.PushConf.as_view(), name='push'),
    path('push/send', views.PushSend.as_view(), name='sendPush'),
    path('general/', views.GeneralConf.as_view(), name='general'),
]

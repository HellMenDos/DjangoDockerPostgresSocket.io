from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bonus/info', views.InfoConf.as_view(),name='info'),
    path('bonus/info/questions', views.QuestionsConf.as_view(),name='questions'),
    path('invate/<str:hashurl>',views.InvationConf.as_view(),name='invate'),
    path('invate/data/<int:num>',views.InvationConfgetOne.as_view(),name='invateData')
]


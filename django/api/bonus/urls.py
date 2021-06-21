from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bonus/info', views.InfoConf.as_view(), name='info'),
    path('bonus/info/questions', views.QuestionsConf.as_view(), name='questions'),
    path('invitation/ios/<str:hashurl>', views.Appst.as_view(), name='invate'),
    path('invitation/android/<str:hashurl>',
         views.Play.as_view(), name='invate'),
    path('invitation/user/<str:hashurl>',
         views.Inv.as_view(), name='invate'),
    path('invitation/data/<int:num>',
         views.InvationConfgetOne.as_view(), name='invateData'),
    path('bonus/relations/get/with/bonus/<int:num>',
         views.BonusGetRelation.as_view(), name='bonusGet'),
    path('bonus/relations/get/with/user/<int:num>',
         views.BonusRelation.as_view(), name='bonusGetuser'),
    path('bonus/relations/insert',
         views.BonusRelationInsert.as_view(), name='bonusInsert'),
    path('bonus/get/with/location/<str:slug>/<int:us>',
         views.BonusGet.as_view(), name='BonusGet'),
    path('bonus/get/with/level/<int:num>/<int:us>',
         views.BonusGetWithLevel.as_view(), name='BonusGetWithLevel'),
    path('bonus/general/get/with/level/<int:num>/<int:us>',
         views.BonusGeneralWithLevel.as_view(), name='BonusGeneralWithLevel'),
    path('bonus/general/get/all/<int:us>',
         views.BonusGeneralGet.as_view(), name='BonusGeneralGet'),
]

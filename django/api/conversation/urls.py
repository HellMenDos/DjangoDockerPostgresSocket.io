from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('company/proposal/', views.InsertProposal.as_view(), name='proposal'),
    path('company/proposals/<int:num>',
         views.getProposals.as_view(), name='proposalOne'),
    path('company/proposals/with/company/<int:num>',
         views.getProposalsCompany.as_view(), name='proppsalCompany'),

    path('applications/', views.GetAllAppl.as_view(), name='GetAllAppl'),
    path('applications/update/photo/',
         views.UpdatePhoto.as_view(), name='GetAllAppl'),
    path('applications/one/with/id/<int:num>',
         views.GetOneAppl.as_view(), name='GetOneAppl'),
    path('applications/company/with/status/<int:num>/<int:status>',
         views.GetCompanyStatusAppl.as_view(), name='GetCompanyStatusAppl'),
    path('applications/user/with/status/<int:num>/<int:status>',
         views.GetUserStatusAppl.as_view(), name='GetUserStatusAppl'),
    path('applications/user/with/active/<int:num>/<str:active>',
         views.GetUserActiveAppl.as_view(), name='GetUserActiveAppl'),
    path('applications/company/with/active/<int:num>/<str:active>',
         views.GetCompanyActiveAppl.as_view(), name='GetCompanyActiveAppl'),
    path('applications/company/<int:num>',
         views.GetOneApplCompany.as_view(), name='GetOneApplCompany'),
    path('applications/user/<int:num>',
         views.GetOneApplUser.as_view(), name='GetOneApplCompany'),
    path('applications/change/active/',
         views.ChangeActiveAppl.as_view(), name='ChangeActiveAppl'),
    path('applications/change/status/',
         views.ChangeStatusAppl.as_view(), name='ChangeStatusAppl'),

    path('message/insert/', views.InsertMessage.as_view(), name=None),
    path('message/one/get/<int:id>', views.getMessage.as_view(), name='getMessage'),
    path('message/get/rooms/<int:id>', views.getRooms.as_view(), name='getRooms'),
    path('message/get/room/<int:companyId>/<int:userId>',
         views.getRoom.as_view(), name='getRoom'),
    path('message/insert/rooms/', views.InsertRoom.as_view(), name='InsertRoom'),

    path('review/insert/', views.InsertReview.as_view(), name='InsertReview'),
    path('review/get/from/<int:id>',
         views.getReviewFrom.as_view(), name='getReviewFrom'),
    path('review/get/to/<int:id>', views.getReviewTo.as_view(), name='getReviewTo'),
    path('adress/get/<str:title>', views.getAdress.as_view(), name='getAdress'),
    path('adress/all/', views.getAllAdress.as_view(), name='getAllAdress'),
]

from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('company/proposal/', views.InsertProposal.as_view(),name='proposal'),
    path('company/proposals/<int:num>', views.getProposals.as_view(),name='proposalOne'),
    path('company/proposals/withcompany/<int:num>', views.getProposalsCompany.as_view(),name='proppsalCompany'),
    
    path('applications/', views.GetAllAppl.as_view(),name='appl'),
    path('applications/one/with/id/<int:num>', views.GetOneAppl.as_view(),name='applOneid'),
    path('applications/company/with/status/<int:num>/<int:status>', views.GetCompanyStatusAppl.as_view(),name='applCompStatus'),
    path('applications/user/with/status/<int:num>/<int:status>', views.GetUserStatusAppl.as_view(),name='applUserStatus'),
    path('applications/user/with/active/<int:num>/<str:active>', views.GetUserActiveAppl.as_view(),name='applUserActive'),
    path('applications/company/with/active/<int:num>/<str:active>', views.GetCompanyActiveAppl.as_view(),name='applCompActive'),
    path('applications/change/active/', views.ChangeActiveAppl.as_view(),name='ChangeActive'),
    path('applications/change/status/', views.ChangeStatusAppl.as_view(),name='ChangeStatus'),
    
    path('message/insert/', views.InsertMessage.as_view(),name='MessageInsert'),
    path('message/one/get/<int:id>', views.getMessage.as_view(),name='MessageOne'),
    path('message/get/rooms/<int:id>', views.getRooms.as_view(),name='getRooms'),
    path('message/insert/rooms/', views.InsertRoom.as_view(),name='inserRooms'),

    path('review/insert/', views.InsertReview.as_view(),name='insertReview'),
    path('review/get/from/<int:id>', views.getReviewFrom.as_view(),name='getFrom'),
    path('review/get/to/<int:id>', views.getReviewTo.as_view(),name='getTo'),
    path('adress/get/<str:title>', views.getAdress.as_view(),name='adressGet'),
]


 
from django.urls import path
from .views import CreateListUser, ListUpdateDeleteUser
from . import views
from django.conf import settings

urlpatterns = [
    path('', CreateListUser.as_view()),
    path('all-users', ListUpdateDeleteUser.as_view()),
    #path('role/<int:role_id>/', views.UserRoleListView.as_view(), name='role-list'),
]
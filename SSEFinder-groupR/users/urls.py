from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('user_authentication/', views.user_authentication, name='user_authentication'),
    path('', views.home_page, name='home'),
    path('add_case/', views.add_case_view, name='add_case'),
    path('add_event/', views.add_event_view, name='add_event'),
    path('link_event/<int:case>', views.link_event_view, name='link_event'),
    path('success/', views.success_view, name='success'),
    path('error/', views.error_view, name='error'),
    path('error_record_exists/', views.error_record_exists_view, name='error_record_exists'),

    path('case_details/<int:case>', views.case_detail, name='case_details'),
    path('sse_list/', views.sse_list, name='sse_list'),
    path('sse_detail/<int:event>', views.sse_detail, name='sse_detail'),
]

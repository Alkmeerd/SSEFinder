from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('user_authentication/', views.user_authentication, name='user_authentication'),
    path('', views.home_page_view, name='home'),
    path('add_case/', views.add_case_view, name='add_case'),
    path('add_event/', views.add_event_view, name='add_event'),
    path('success/', views.success_view, name='success'),
    path('error/', views.error_view, name='error'),

    path('case_events_details/<int:case>', views.ViewLocCase, name='case_events_details'),
    path('date_range/', views.SSE_date_range, name='date_range'),
    path('sse_display/<int:event>', views.sse_display, name='sse_display'),
]

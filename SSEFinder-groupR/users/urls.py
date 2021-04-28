from django.urls import path
from . import views


urlpatterns = [

    path('user_authentication/', views.user_authentication, name='user_authentication'),
    path('home_page', views.home_page_view.as_view(), name='home'),
    path('add_case/', views.add_case_view, name='add_case'),
    path('add_event/', views.add_event_view, name='add_event'),
    path('success/', views.success_view.as_view(), name='success'),
    path('error/', views.error_view.as_view(), name='error'),

    path('case_events_details/<int:case>', views.ViewLocCase.as_view(), name='case_events_details'),
]

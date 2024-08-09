from django.urls import path
from .views import index,register,login_user,logout_user,speakers,dashboard,about,tickets,ticket_details,rent_venue,shows_events
urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('loginuser', login_user, name='login_user'),
    path('logoutuser', logout_user, name='logout_user'),
    path('speakers', speakers, name='speakers'),
    path('dashboard', dashboard, name='dashboard'),
    path('about', about, name='about'),
    path('tickets', tickets, name='tickets'),
    path('ticketdetails', ticket_details, name='ticket_details'),
    path('rentvenue', rent_venue, name='rent_venue'),
    path('showsevents', shows_events, name='shows_events')
   
    
]
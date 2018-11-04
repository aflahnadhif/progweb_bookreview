from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('loggedhome/', views.loggedhome, name='loggedhome'),
    path('<int:book_id>/', views.details, name='details'),
    path('log', views.log_in, name='logging_in'),
    path('reg', views.register, name='reg'),
    path('out', views.log_out, name='logging_out'),
    path('postit/<int:bookid>', views.postit)
]
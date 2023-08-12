from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('update_record/<int:id>',views.update_record,name='update_record'),
    path('delete_record/<int:id>',views.delete_record,name='delete'),
    path('add_record/',views.add_record,name='add'),
]

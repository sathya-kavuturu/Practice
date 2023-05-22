from django.urls import path
from .views import *


urlpatterns = [
    path('api/', Student_List_Create.as_view(), name = 'student_list_create' ),
    path('action/<int:pk>', Student_Dis_Up_Del.as_view(), name = 'student_retrieve_update_delete' ),
   

]
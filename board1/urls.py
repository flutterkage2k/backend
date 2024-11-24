from django.urls import path
from .import views

urlpatterns = [
	path('api/boardpost/list/',views.boardPost_list, name='list'),
	path('api/boardpost/details/<int:id>/',views.boardPost_details, name='list_details')
]

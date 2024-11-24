from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from .models import BoardPost 
from .serializers import BoardPostSerializer 
from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view([ 'GET', 'POST' ])
def boardPost_list(request):
	if request.method == "GET":
		boardPost = BoardPost.objects.all()
		serializer = BoardPostSerializer (boardPost, many = True)
		return Response(serializer.data)
	
	if request.method == "POST":
		serializer = BoardPostSerializer(data = request.data)
		if serializer.is_valid():
				serializer.save()
				return Response({"msg": "Success"}, status = status.HTTP_201_CREATED)
		else:
				return Response({"error": "Failed"}, status = status.HTTP_404_NOT_FOUND)
		
@api_view([ 'GET', 'PUT', 'PATCH', 'DELETE' ])
def boardPost_details(request, id = None):
	if request.method	 =="GET":
		boardPost = get_object_or_404(BoardPost,id=id)
		serializer = BoardPostSerializer(boardPost, many = False)
		return Response(serializer.data)
	
	if request.method	 =="PUT":
		boardPost = get_object_or_404(BoardPost,id=id)
		serializer = BoardPostSerializer(boardPost, data = request.data)
		if serializer.is_valid():
				serializer.save()
				return Response({"msg": "Success"}, status = status.HTTP_201_CREATED)
		else:
				return Response({"error": "Failed"}, status = status.HTTP_404_NOT_FOUND)
		

	if request.method	 =="PATCH":
		boardPost = get_object_or_404(BoardPost,id=id)
		serializer = BoardPostSerializer(boardPost, data = request.data, partial= True)
		if serializer.is_valid():
				serializer.save()
				return Response({"msg": "Success"}, status = status.HTTP_201_CREATED)
		else:
				return Response({"error": "Failed"}, status = status.HTTP_404_NOT_FOUND)
 
	if request.method	 =="DELETE":
		boardPost = get_object_or_404(BoardPost,id=id)
		boardPost.delete()
		return Response({"msg": "Successfully deleted"}, status = status.HTTP_201_CREATED)
		
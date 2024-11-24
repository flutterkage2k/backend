from rest_framework import serializers 
from .models import BoardPost

class BoardPostSerializer (serializers.ModelSerializer):
	class Meta:
		model = BoardPost
		fields = "__all__"

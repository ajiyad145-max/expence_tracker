from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework.response import Response

class SignUpView(APIView):
    def post(self,request):
        form_data=request.data 
        serializers_instance=UserSerializer(data=form_data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data)
        else:
            return Response(serializers_instance.errors)


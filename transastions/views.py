from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions,authentication
from rest_framework.response import Response

from transastions.models import Expense
from transastions.serializers import ExpenseSerializer

class ExpenseListCreateView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        auth_user=request.user
        qs=Expense.objects.filter(owner=auth_user)
        serializers_instance=ExpenseSerializer(qs,many=True)
        return Response(serializers_instance.data)

    def post(self,request):
        form_data=request.data
        auth_user=request.user
        serializers_instance=ExpenseSerializer(data=form_data)
        if serializers_instance.is_valid():
            serializers_instance.save(owner=auth_user)
            return Response(serializers_instance.data)
        else:
            return Response(serializers_instance.errors)
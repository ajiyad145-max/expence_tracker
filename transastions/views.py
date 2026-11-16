from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions,authentication
from rest_framework.response import Response

from transastions.models import Expense
from transastions.serializers import ExpenseSerializer

from transastions.permissions import IsOwner

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
            serializers_instance.save(owner = auth_user)
            return Response(serializers_instance.data)
        else:
            return Response(serializers_instance.errors)

class ExpenseRetrieveUpdateDeleteView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    # permission_classes=[permissions.IsAuthenticated]

    permission_classes=[IsOwner]


    def get(self,request,pk=None):
        # qs=Expense.objects.get(id=pk)
        qs=get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,qs)

        serializers_instance=ExpenseSerializer(qs)
        return Response(serializers_instance.data)

    def put(self,request,pk=None):
        # instance=Expense.objects.get(id=pk)
        instance=get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        form_data=request.data
        serializers_instance=ExpenseSerializer(data=form_data,instance=instance)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data)
        else:
            return Response(serializers_instance.errors)

    def delete(self,request,pk=None):
        # qs=Expense.objects.get(id=pk).delete()
        qs=get_object_or_404(Expense,id=pk)
        qs.delete()

        self.check_object_permissions(request,qs)

        return Response({"message":"Deleted"})
from rest_framework import serializers
from transastions.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        feilds="__all__"
        read_only_feilds=["id","owner","created_at"]

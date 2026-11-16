from rest_framework import serializers
from transastions.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields="__all__"
        read_only_fields=["id","owner","created_at"]

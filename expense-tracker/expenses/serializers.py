

# # expenses/serializers.py
# from rest_framework import serializers
# from .models import Category, Expense, Budget

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']

# class ExpenseSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
#     category_id = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all(), source='category', write_only=True
#     )
#     user = serializers.ReadOnlyField(source='user.username')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Filter categories to only those belonging to the authenticated user
#         if self.context.get('request') and self.context['request'].user.is_authenticated:
#             self.fields['category_id'].queryset = Category.objects.filter(user=self.context['request'].user)

#     class Meta:
#         model = Expense
#         fields = ['id', 'user', 'category', 'category_id', 'amount', 'description', 'date', 'created_at']

# class BudgetSerializer(serializers.ModelSerializer):
#     category_id = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all(), source='category', write_only=True
#     )
#     category = CategorySerializer(read_only=True)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Filter categories to only those belonging to the authenticated user
#         if self.context.get('request') and self.context['request'].user.is_authenticated:
#             self.fields['category_id'].queryset = Category.objects.filter(user=self.context['request'].user)

#     class Meta:
#         model = Budget
#         fields = ['id', 'category', 'category_id', 'amount', 'month']


from rest_framework import serializers
from .models import Category, Expense, Budget

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Expense
        fields = ['id', 'category', 'category_id', 'amount', 'currency', 'base_amount', 'description', 'date']

class BudgetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Budget
        fields = ['id', 'category', 'category_id', 'amount', 'month']
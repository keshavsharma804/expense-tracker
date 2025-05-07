


# # expenses/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Category(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)

#     class Meta:
#         unique_together = ('user', 'name')  # Ensure category names are unique per user

#     def __str__(self):
#         return self.name

# class Expense(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField(blank=True)
#     date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.description or 'Expense'} - {self.amount}"

# class Budget(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     month = models.CharField(max_length=7)  # Format: "YYYY-MM", e.g., "2025-05"

#     class Meta:
#         unique_together = ('user', 'category', 'month')  # Ensure only one budget per user per category per month

#     def __str__(self):
#         return f"Budget for {self.category.name} in {self.month}: {self.amount}"





from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'name')  # Ensure category names are unique per user

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')  # e.g., USD, EUR, INR
    base_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Amount in base currency (USD)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description or 'Expense'} - {self.amount} {self.currency}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=7)  # Format: "YYYY-MM", e.g., "2025-05"

    class Meta:
        unique_together = ('user', 'category', 'month')  # Ensure only one budget per user per category per month

    def __str__(self):
        return f"Budget for {self.category.name} in {self.month}: {self.amount}"
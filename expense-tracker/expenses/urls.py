


# expenses/urls.py
# from django.urls import path
# from .views import (
#     CategoryListView,
#     ExpenseListCreateView,
#     ExpenseDetailView,
#     ExpenseSummaryView,
#     BudgetListCreateView,
#     CategorySpendingView
# )

# urlpatterns = [
#     path('categories/', CategoryListView.as_view(), name='category-list'),
#     path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
#     path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
#     path('summary/', ExpenseSummaryView.as_view(), name='expense-summary'),
#     path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
#     path('category-spending/', CategorySpendingView.as_view(), name='category-spending'),
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'expenses', views.ExpenseViewSet, basename='expense')
router.register(r'budgets', views.BudgetViewSet, basename='budget')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', views.SummaryView.as_view(), name='expense-summary'),
    path('category-spending/', views.CategorySpendingView.as_view(), name='category-spending'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
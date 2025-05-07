

# from rest_framework import viewsets, generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Category, Expense, Budget
# from .serializers import CategorySerializer, ExpenseSerializer, BudgetSerializer
# from django.db.models import Sum
# from rest_framework.exceptions import PermissionDenied
# import calendar
# from datetime import datetime
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# import requests

# class CategoryViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CategorySerializer

#     def get_queryset(self):
#         if not self.request.user.is_authenticated:
#             raise PermissionDenied("Authentication credentials were not provided.")
#         return Category.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         if not self.request.user.is_authenticated:
#             raise PermissionDenied("Authentication credentials were not provided.")
#         serializer.save(user=self.request.user)

# class ExpenseViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = ExpenseSerializer

#     def get_queryset(self):
#         return Expense.objects.filter(user=self.request.user)

#     def fetch_exchange_rate(self, from_currency, to_currency='USD'):
#         api_key = 'YOUR_API_KEY'  # Replace with your ExchangeRate-API key
#         url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
#         try:
#             response = requests.get(url)
#             data = response.json()
#             if response.status_code != 200 or data.get('result') != 'success':
#                 raise Exception('Failed to fetch exchange rates')
#             rate = data['conversion_rates'].get(to_currency)
#             if not rate:
#                 raise Exception(f'Conversion rate for {to_currency} not found')
#             return rate
#         except Exception as e:
#             # Fallback to a default rate or handle the error
#             raise Exception(f'Error fetching exchange rate: {str(e)}')

#     def perform_create(self, serializer):
#         currency = self.request.data.get('currency', 'USD')
#         amount = float(self.request.data.get('amount'))

#         # Convert amount to base currency (USD)
#         if currency != 'USD':
#             rate = self.fetch_exchange_rate(currency, 'USD')
#             base_amount = amount * rate
#         else:
#             base_amount = amount

#         serializer.save(
#             user=self.request.user,
#             currency=currency,
#             base_amount=base_amount
#         )

#     def perform_update(self, serializer):
#         currency = self.request.data.get('currency', serializer.instance.currency)
#         amount = float(self.request.data.get('amount', serializer.instance.amount))

#         # Convert amount to base currency (USD)
#         if currency != 'USD':
#             rate = self.fetch_exchange_rate(currency, 'USD')
#             base_amount = amount * rate
#         else:
#             base_amount = amount

#         serializer.save(
#             currency=currency,
#             base_amount=base_amount
#         )

# class SummaryView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         month = request.query_params.get('month')
#         if not month:
#             return Response({'error': 'Month parameter is required'}, status=400)

#         try:
#             year, month = map(int, month.split('-'))
#             _, last_day = calendar.monthrange(year, month)
#             start_date = datetime(year, month, 1)
#             end_date = datetime(year, month, last_day)

#             expenses = Expense.objects.filter(
#                 user=user,
#                 date__range=[start_date, end_date]
#             ).values('category__name').annotate(total=Sum('base_amount'))  # Use base_amount for summary

#             return Response(expenses)

#         except ValueError:
#             return Response({'error': 'Invalid month format. Use YYYY-MM'}, status=400)

# class BudgetViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BudgetSerializer

#     def get_queryset(self):
#         return Budget.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class CategorySpendingView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         month = request.query_params.get('month')
#         if not month:
#             return Response({'error': 'Month parameter is required'}, status=400)

#         try:
#             year, month = map(int, month.split('-'))
#             _, last_day = calendar.monthrange(year, month)
#             start_date = datetime(year, month, 1)
#             end_date = datetime(year, month, last_day)

#             expenses = Expense.objects.filter(
#                 user=user,
#                 date__range=[start_date, end_date]
#             ).values('category_id').annotate(total_spending=Sum('base_amount'))  # Use base_amount

#             return Response(expenses)

#         except ValueError:
#             return Response({'error': 'Invalid month format. Use YYYY-MM'}, status=400)

# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not username or not email or not password:
#             return Response(
#                 {'error': 'Username, email, and password are required'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         if User.objects.filter(username=username).exists():
#             return Response(
#                 {'error': 'Username already exists'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         if User.objects.filter(email=email).exists():
#             return Response(
#                 {'error': 'Email already exists'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             user = User.objects.create_user(
#                 username=username,
#                 email=email,
#                 password=password
#             )
#             user.save()

#             # Create default categories for the new user
#             default_categories = ['Food', 'Transport', 'Entertainment', 'Bills', 'Other']
#             for category_name in default_categories:
#                 Category.objects.create(user=user, name=category_name)

#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user': {
#                     'id': user.id,
#                     'username': user.username,
#                     'email': user.email
#                 }
#             }, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             return Response(
#                 {'error': str(e)},
#                 status=status.HTTP_400_BAD_REQUEST
#             )




import requests
import logging
from django.core.cache import cache
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Category, Expense, Budget
from .serializers import CategorySerializer, ExpenseSerializer, BudgetSerializer
from django.db.models import Sum
from rest_framework.exceptions import PermissionDenied
import calendar
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

# Set up logging
logger = logging.getLogger('expenses')

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Authentication credentials were not provided.")
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Authentication credentials were not provided.")
        serializer.save(user=self.request.user)

class ExpenseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def fetch_exchange_rate(self, from_currency, to_currency='USD'):
        # Check cache first
        cache_key = f'exchange_rate_{from_currency}_{to_currency}'
        cached_rate = cache.get(cache_key)
        if cached_rate:
            logger.info(f'Fetched exchange rate from cache: {from_currency} to {to_currency}')
            return cached_rate

        # Replace with your actual API key
        api_key = 'YOUR_API_KEY'  # Replace with your ExchangeRate-API key
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise for HTTP errors (e.g., 403, 429)
            data = response.json()
            if data.get('result') != 'success':
                raise ValueError('Failed to fetch exchange rates: API returned unsuccessful result')
            rate = data['conversion_rates'].get(to_currency)
            if not rate:
                raise ValueError(f'Conversion rate for {to_currency} not found')
            
            # Cache the rate for 24 hours
            cache.set(cache_key, rate, timeout=24*60*60)
            logger.info(f'Successfully fetched and cached exchange rate: {from_currency} to {to_currency}')
            return rate
        except (requests.RequestException, ValueError, KeyError) as e:
            logger.error(f'Error fetching exchange rate from {from_currency} to {to_currency}: {str(e)}')
            raise Exception(f'Error fetching exchange rate: {str(e)}')

    def perform_create(self, serializer):
        currency = self.request.data.get('currency', 'USD')
        amount = float(self.request.data.get('amount'))
        base_amount = amount

        # Convert amount to base currency (USD)
        if currency != 'USD':
            try:
                rate = self.fetch_exchange_rate(currency, 'USD')
                base_amount = amount * rate
            except Exception as e:
                logger.warning(f'Failed to fetch exchange rate for {currency}. Saving expense without conversion.')
                # Fallback: Save expense without conversion
                serializer.save(
                    user=self.request.user,
                    currency=currency,
                    base_amount=base_amount  # Use original amount as base_amount
                )
                return Response(
                    {'error': str(e), 'detail': 'Expense saved without currency conversion.'},
                    status=status.HTTP_201_CREATED
                )

        serializer.save(
            user=self.request.user,
            currency=currency,
            base_amount=base_amount
        )

    def perform_update(self, serializer):
        currency = self.request.data.get('currency', serializer.instance.currency)
        amount = float(self.request.data.get('amount', serializer.instance.amount))
        base_amount = amount

        # Convert amount to base currency (USD)
        if currency != 'USD':
            try:
                rate = self.fetch_exchange_rate(currency, 'USD')
                base_amount = amount * rate
            except Exception as e:
                logger.warning(f'Failed to fetch exchange rate for {currency} during update. Saving expense without conversion.')
                # Fallback: Save expense without conversion
                serializer.save(
                    currency=currency,
                    base_amount=base_amount  # Use original amount as base_amount
                )
                return Response(
                    {'error': str(e), 'detail': 'Expense updated without currency conversion.'},
                    status=status.HTTP_200_OK
                )

        serializer.save(
            currency=currency,
            base_amount=base_amount
        )

class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        month = request.query_params.get('month')
        if not month:
            return Response({'error': 'Month parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year, month = map(int, month.split('-'))
            _, last_day = calendar.monthrange(year, month)
            start_date = datetime(year, month, 1)
            end_date = datetime(year, month, last_day)

            expenses = Expense.objects.filter(
                user=user,
                date__range=[start_date, end_date]
            ).values('category__name').annotate(total=Sum('base_amount'))  # Use base_amount for summary

            return Response(expenses, status=status.HTTP_200_OK)

        except ValueError as e:
            logger.error(f'Invalid month format in SummaryView: {str(e)}')
            return Response({'error': 'Invalid month format. Use YYYY-MM'}, status=status.HTTP_400_BAD_REQUEST)

class BudgetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategorySpendingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        month = request.query_params.get('month')
        if not month:
            return Response({'error': 'Month parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year, month = map(int, month.split('-'))
            _, last_day = calendar.monthrange(year, month)
            start_date = datetime(year, month, 1)
            end_date = datetime(year, month, last_day)

            expenses = Expense.objects.filter(
                user=user,
                date__range=[start_date, end_date]
            ).values('category_id').annotate(total_spending=Sum('base_amount'))  # Use base_amount

            return Response(expenses, status=status.HTTP_200_OK)

        except ValueError as e:
            logger.error(f'Invalid month format in CategorySpendingView: {str(e)}')
            return Response({'error': 'Invalid month format. Use YYYY-MM'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response(
                {'error': 'Username, email, and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Username already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'Email already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()

            # Create default categories for the new user
            default_categories = ['Food', 'Transport', 'Entertainment', 'Bills', 'Other']
            for category_name in default_categories:
                Category.objects.create(user=user, name=category_name)

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(f'Error during user registration: {str(e)}')
            return Response(
                {'error': f'Failed to register user: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
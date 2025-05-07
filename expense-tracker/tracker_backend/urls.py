# # tracker_backend/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('expenses.urls')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]






# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from django.http import HttpResponse

# def homepage(request):
#     return HttpResponse("<h1>Welcome to Expense Tracker API!</h1><p>Visit /api/ for available endpoints.</p>")

# urlpatterns = [
#     path('', homepage),  # Add homepage view here
#     path('admin/', admin.site.urls),
#     path('api/', include('expenses.urls')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]



from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse

def homepage(request):
    return HttpResponse(
        "<h1>Welcome to Expense Tracker API!</h1>"
        "<p>Available endpoints:</p>"
        "<ul>"
        "<li><b>/api/</b> - Main API endpoints (categories, expenses, budgets, etc.)</li>"
        "<li><b>/api/register/</b> - Register a new user (POST)</li>"
        "<li><b>/api/token/</b> - Obtain JWT token pair (POST)</li>"
        "<li><b>/api/token/refresh/</b> - Refresh JWT token (POST)</li>"
        "<li><b>/admin/</b> - Admin panel</li>"
        "</ul>"
    )

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('api/', include('expenses.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

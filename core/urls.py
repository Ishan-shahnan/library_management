from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import api_root_view


schema_view = get_schema_view(
    openapi.Info(
        title="Library Management System API",
        default_version='v1',
        description="""
        A simple Library Management System API built with Django REST Framework.
        
        ## Features
        - Books Management: Add, view, update, and delete books
        - Authors Management: Manage book authors
        - Members Management: Manage library members
        - Borrowing System: Borrow and return books
        - JWT Authentication: User login and registration
        - Role-based Permissions: Admin and member access control
        
        ## User Roles
        - Librarian (Admin): Can manage all books, authors, and members
        - Member (User): Can view books and authors, borrow and return books
        
        ## Authentication
        1. Register: POST /auth/users/
        2. Login: POST /auth/jwt/create/
        3. Use token in requests: Authorization: Bearer <token>
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@library.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'), name='api-root'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, MemberViewSet, BorrowView, ReturnView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrow/', BorrowView.as_view(), name='borrow-book'),
    path('return/', ReturnView.as_view(), name='return-book'),
]
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book, Author, Member, BorrowRecord
from .serializers import BookSerializer, AuthorSerializer, MemberSerializer, BorrowRecordSerializer


class BookViewSet(viewsets.ModelViewSet):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class AuthorViewSet(viewsets.ModelViewSet):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class MemberViewSet(viewsets.ModelViewSet):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]


class BorrowView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = BorrowRecordSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.validated_data['book']
            if not book.availability_status:
                return Response(
                    {"error": "Book is not available for borrowing"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            book.availability_status = False
            book.save()
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            record_id = request.data.get('id')
            if not record_id:
                return Response(
                    {"error": "Borrow record ID is required"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            borrow_record = BorrowRecord.objects.get(id=record_id)
            
            book = borrow_record.book
            book.availability_status = True
            book.save()
            
            borrow_record.delete()
            
            return Response(
                {"message": "Book returned successfully"}, 
                status=status.HTTP_200_OK
            )
        except BorrowRecord.DoesNotExist:
            return Response(
                {"error": "Borrow record not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Author, Member, BorrowRecord
from .serializers import BookSerializer, AuthorSerializer, MemberSerializer, BorrowRecordSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BorrowRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            record_id = request.data.get('id')
            borrow_record = BorrowRecord.objects.get(id=record_id)
            # Add logic here to update book status, etc.
            borrow_record.delete()
            return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
        except BorrowRecord.DoesNotExist:
            return Response({"message": "Borrow record not found"}, status=status.HTTP_404_NOT_FOUND)
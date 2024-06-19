from rest_framework.viewsets import ModelViewSet

from books.api.serializers import BookSerializers
from books.models import Book


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()

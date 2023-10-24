## convert our model instances into JSON 

from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'lastname')

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

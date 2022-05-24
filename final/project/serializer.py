from .models import Book, Journal, User
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    num_pages = serializers.IntegerField()
    genre = serializers.CharField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'description', 'created_at', 'num_pages', 'genre')


class JournalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    type = serializers.CharField()
    publisher = serializers.CharField()

    class Meta:
        model = Journal
        fields = ('id', 'name', 'price', 'description', 'created_at', 'type', 'publisher')

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
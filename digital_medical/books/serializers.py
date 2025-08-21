from rest_framework import serializers
from .models import BooksModel

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'  # or list fields manually if you want control
        read_only_fields = ['created_at', 'updated_at']  # prevent editing via API
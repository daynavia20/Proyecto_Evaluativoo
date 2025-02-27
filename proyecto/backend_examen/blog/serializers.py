from rest_framework import serializers
from .models import Blog, Comentario

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'author', 'created_at', 'updated_at']
        

class BlogOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'text', 'author', 'created_at', 'updated_at']
        
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['blog', 'author', 'text', 'created_at']
        

class ComentarioOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'blog', 'author', 'text', 'created_at']
        
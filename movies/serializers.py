from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    rating = serializers.CharField()
    synopsis = serializers.CharField()
    added_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

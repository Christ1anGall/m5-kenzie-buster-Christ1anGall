from rest_framework import serializers

from .models import Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    rating = serializers.CharField()
    synopsis = serializers.CharField()
    added_by = serializers.CharField(read_only=True)

    def create(self, validated_data: dict) -> Movie:
        movie = Movie.objects.create(**validated_data)
        return movie


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.CharField(read_only=True)
    price = serializers.FloatField()

    def get_title(self, obj: MovieOrder):
        return obj.movie.title

    def get_buyed_by(self, obj: MovieOrder):
        return obj.user.email

    def create(self, validated_data: dict) -> MovieOrder:
        movieOrder = MovieOrder.objects.create(**validated_data)
        return movieOrder

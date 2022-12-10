from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from .models import Movie


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request) -> Response:
        return Response(status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("=" * 100)
        print(request.user.email)
        print("=" * 100)
        serializer.save(added_by=request.user.email)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

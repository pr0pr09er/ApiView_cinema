from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Films, Genre, Poster, Director
from .serializers import FilmSerializer, GenreSerializer, PosterSerializer, DirectorSerializer


class FilmList(ListAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer



class FilmView(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class GenreList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PosterList(ListAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class PosterView(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class DirectorList(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

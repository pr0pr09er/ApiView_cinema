from django.contrib import admin
from django.urls import path
from film.views import FilmList, FilmView, DirectorList, DirectorView, GenreList, GenreView, PosterList, \
    PosterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/films/', FilmList.as_view(), name="film_list"),
    path('api/v1/films/<int:pk>/', FilmView.as_view(), name="film_view"),
    path('api/v1/directors/', DirectorList.as_view(), name="director_list"),
    path('api/v1/directors/<int:pk>', DirectorView.as_view(), name="director_view"),
    path('api/v1/genres/', GenreList.as_view(), name="genre_list"),
    path('api/v1/genres/<int:pk>/', GenreView.as_view(), name="genre_view"),
    path('api/v1/posters/', PosterList.as_view(), name="poster_list"),
    path('api/v1/posters/<int:pk>/', PosterView.as_view(), name="poster_view"),
]

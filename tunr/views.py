# from django.shortcuts import render, redirect
# from django.http import JsonResponse
from .models import Artist, Song
from rest_framework import generics
from .serializers import ArtistSerializer
from .serializers import SongSerializer
from .forms import ArtistForm, SongForm
# from .forms import ArtistForm, SongForm
# Create your views here.

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# def artist_list(request):
#     artists = Artist.objects.all()
#     return render(request, 'tunr/artist_list.html', {'artists': artists})

#     # IF I WANT TO CREATE AN API
#     # artists = Artist.objects.all().values('name', 'nationality', 'photo_url')# only grab some attributes from our database, else we can't serialize it.
#     # artist_list = list(artists)# convert our artists to a list instead of QuerySet
#     # return JsonResponse(artist_list, safe=False)# safe=False is needed if the first parameter is not a dictionary.
    
# def song_list(request):
#     songs = Song.objects.all()
#     return render(request, 'tunr/song_list.html', {'songs': songs})

# def artist_detail(request, pk):
#     artist = Artist.objects.get(id=pk)
#     return render(request, 'tunr/artist_detail.html', {'artist': artist})

# def song_detail(request, pk):
#     song = Song.objects.get(id=pk)
#     return render(request, 'tunr/song_detail.html', {'song': song})

# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm()
#     return render(request, 'tunr/artist_form.html', {'form': form})

# def song_create(request):
#     if request.method == 'POST':
#         form = SongForm(request.POST)
#         if form.is_valid():
#             song = form.save()
#             return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm()
#     return render(request, 'tunr/song_form.html', {'form': form})

# # tunr/views.py
# def artist_edit(request, pk):
#     artist = Artist.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ArtistForm(request.POST, instance=artist)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm(instance=artist)
#     return render(request, 'tunr/artist_form.html', {'form': form})

# def song_edit(request, pk):
#     song = Song.objects.get(pk=pk)
#     if request.method == "POST":
#         form = SongForm(request.POST, instance=song)
#         if form.is_valid():
# 	        song = form.save()
#         return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm(instance=song)
#     return render(request, 'tunr/song_form.html', {'form': form})

# def artist_delete(request, pk):
# #     # One way
#     Artist.objects.get(id=pk).delete()
#     return redirect('artist_list')
# #     # Another way
# #     # artist = Artist.objects.get(id=pk)
# #     # artist.delete()
# #     # return redirect('artist_list')

# def song_delete(request, pk):
#     Song.objects.get(id=pk).delete()
#     return redirect('song_list')
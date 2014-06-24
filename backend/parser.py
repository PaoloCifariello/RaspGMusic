import dataset

from models import *

class Parser:

    def __init__(self):
        self.artistId = 1
        self.albumId = 1

        self.artists = []
        self.albums = []
        self.tracks = []

    def insert(self, db):
        tr = db.create_table('tracks', primary_id='gid', primary_type='String')
        ar = db.create_table('artists', primary_id='gid', primary_type='String')
        al = db.create_table('albums', primary_id='gid', primary_type='String')

        for track in self.tracks:
            tr.insert(dict(gid = track.gid, name = track.name, artistId = track.artistId, albumId = track.albumId, track_no = track.track_no,))

        for artist in self.artists:
            ar.insert(dict(gid = artist.gid, name = artist.name, art_url = artist.art_url))

        for album in self.albums:
            al.insert(dict(gid = album.gid, name = album.name, artistId = album.artistId, year = album.year, art_url = album.art_url))

    def parse(self, db, data):

        for song in data:
            track = Track()
            
            artist = self.parse_artist(song)
            track.artistId = artist.gid

            album = self.parse_album(song, artist)     
            track.albumId = album.gid

            track.name = song['title']
            track.gid = song['id']
            
            try:
                track.track_no = song['trackNumber']
            except:
                track.track_no = 0

            self.tracks.append(track)

        self.insert(db)

    def parse_artist(self, song):

        if song['albumArtist'] == "":
            if song['artist'] == "":
                a = "Unknown Artist"
            else:
                a = song['artist']
        else:
            a = song['albumArtist']

        artist = self.is_present_artist(a)
        
        if artist == None:
            self.artistId +=1
            artist = Artist(self.artistId)
            artist.name = a

            try:
                artist.art_url = song['artistArtRef'][0]['url']
            except:
                pass

            self.artists.append(artist)
            print "Added artist: " + a

        return artist

    def parse_album(self, song, artist):

        album = self.is_present_album(song['album'], artist.gid)

        if album == None:
            self.albumId += 1
            album = Album(self.albumId)
            album.name = song['album']
            album.artistId = artist.gid
            try:
                album.year = song['year']
            except:
                pass

            try:
                album.art_url = song['albumArtRef'][0]['url']
            except:
                pass

            self.albums.append(album)

        return album
    
    def is_present_artist(self, name):
        for artist in self.artists:
            if artist.name == name:
                return artist

        return None

    def is_present_album(self, album_name, artistId):
        for album in self.albums:
            if album.name == album_name and album.artistId == artistId:
                return album

        return None
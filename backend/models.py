class Artist:
	def __init__(self, id):
		self.gid = id
		self.name = self.art_url = None

class Album:
	def __init__(self, id):
		self.gid = id
		self.name = self.artistId = self.year = self.art_url = None

class Track:
	def __init__(self):
		self.gid = self.name = self.artistId = self.albumId = self.track_no = None

class Playlist:
	def __init__(self):
		self.gid = self.name = self.pid = None
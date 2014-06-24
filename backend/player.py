import pygame, StringIO, setting, sys

from gmusicapi import Webclient

class Player:

	def __init__(self, library_manager):
		pygame.init()
		pygame.mixer.init()

		self.library_manager = library_manager
		self.webapi = Webclient()

		try:
			self.webapi.login(setting.GUSER, setting.GPASS)
		except:
			sys.stderr.write('Problem with authentication on Google server\n')


	def play(self, songId):
		f = open('tostream.mp3', 'w')
		song = self.webapi.get_stream_audio(songId)
		f.write(song)
		f.close()
		#songFile = StringIO.StringIO(song)
		
		pygame.mixer.music.load('tostream.mp3')
		pygame.mixer.music.play()

		print('streaming audio: ' + songId)

		while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)

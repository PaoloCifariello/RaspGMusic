
import pickle, setting, dataset, os

from gmusicapi import Mobileclient
from parser import Parser

class LibraryManager:

	def __init__(self):
		
		self.parser = Parser()
		
		# Remove old database and creates new one
		self.init_db()

	""" Delete old database and creates the new one """
	def init_db(self):

		if setting.UPDATE_DB_ON_STARTUP:
			self.refresh_db()
		else:
			self.db = dataset.connect('sqlite:///' + setting.db_path)

	def refresh_db(self):
		try:
			os.remove(setting.db_path)
		except OSError:
			pass

		data = self.get_data()

		self.db = dataset.connect('sqlite:///' + setting.db_path)
		self.parser.parse(self.db, data)

	def get_data(self):
		mobileapi = Mobileclient()
		mobileapi.login(setting.GUSER, setting.GPASS)
		library = mobileapi.get_all_songs()
		mobileapi.logout()
		
		return library

	def get_tracks(self):
		return self.db['tracks'].all()

	def get(self):
		lorde_traks = [track['id'] for track in self.libdata if track['artist'] == 'Lorde']
		return lorde_traks[0]
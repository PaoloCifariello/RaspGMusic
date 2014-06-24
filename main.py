
from backend.player import Player
from backend.library_manager import LibraryManager
from frontend.web_listener import WebListener

def main():
	
	library_manager = LibraryManager()
	
	player = Player(library_manager)
	listener = WebListener(player, library_manager)

	player.play()
	

if __name__ == '__main__':
    main()
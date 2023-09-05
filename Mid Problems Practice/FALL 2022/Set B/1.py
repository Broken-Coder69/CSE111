class Spotify:
    def __init__(self, *args):
        self.args = args
        self.genre = ""
        self.songs = []
        
    def show_playlist(self):
        self.genre = str(self.args[0])
        self.songs = list(self.args[1:])
        
        print("Output:")
        print(f"Genre: {self.genre}")
        return f"Song list: {', '.join(self.songs)}"



rock= Spotify("Heavy Metal", "This Fire Burns", "Here I Am")
print(rock.show_playlist())


# Output:
# Genre: Heavy Metal
# Song list: This Fire Burns, Here I Am
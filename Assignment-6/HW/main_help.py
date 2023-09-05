class Movie:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration

    def movieInfo(self):
        return f"Movie Name:{self.name}\nMovie Genre:{self.genre}\nMovie Duration:{self.duration} minutes."

    @classmethod
    def createMovie_fromString(cls, string):
        name, genre, duration = string.split('-')
        return cls(name, genre, int(duration))


class StarCinema:
    all_branch_info = {}

    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.movie_list = []
        self.update_branch_info()

    def update_branch_info(self):
        StarCinema.all_branch_info[self.branch_name] = self.movie_list

    def addMovies(self, *movie_objects):
        for movie in movie_objects:
            if movie not in self.movie_list:
                self.movie_list.append(movie)
        self.update_branch_info()

    def removeMovie(self, movie_object):
        if movie_object in self.movie_list:
            self.movie_list.remove(movie_object)
            self.update_branch_info()

    @classmethod
    def check(cls, movie_name):
        found_in_branches = []
        for branch, movie_list in cls.all_branch_info.items():
            for movie in movie_list:
                if movie.name == movie_name:
                    found_in_branches.append(branch)
                    print(f"{movie.movieInfo()}\n{'*' * 30}")
                    break
        if not found_in_branches:
            print(f"Movie '{movie_name}' is not being streamed at any branch.")

    @classmethod
    def showAllBranchInfo(cls):
        for branch, movie_list in cls.all_branch_info.items():
            print(f"Branch Name: {branch}")
            for idx, movie in enumerate(movie_list, start=1):
                print(f"Movie No: {idx}")
                print(movie.movieInfo())
                print("-" * 30)
            print("#" * 30)


# Creating Movie objects
movie1 = Movie('Oppenheimer', 'Biographical Drama', 180)
movie2 = Movie('Barbie', 'Fantasy Comedy', 114)
movie3 = Movie('Mission: Impossible – Dead Reckoning Part One', 'Action', 163)

movie4 = Movie.createMovie_fromString('Prohelika-Drama-153')

# Creating StarCinema branches
branch1 = StarCinema('Mohakhali')
branch2 = StarCinema('Mirpur')

# Adding movies to branches
branch1.addMovies(movie1, movie2, movie4)
branch1.addMovies(movie1, movie3)
branch2.addMovies(movie1, movie2, movie3)

# Removing a movie from a branch
branch1.removeMovie(movie2)
branch2.removeMovie(movie1)

# Checking movie details
StarCinema.check('Oppenheimer')
StarCinema.check('Sound of Freedom')

# Showing all branch information
StarCinema.showAllBranchInfo()

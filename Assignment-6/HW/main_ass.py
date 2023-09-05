class Movie:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration
        
        
    def movieInfo(self):
        print(f"Movie Name: {self.name}")
        print(f"Movie Genre:{self.genre}")
        return (f"Movie Duration: {self.duration} minutes")
    
    

    
    @classmethod
    def createMovie_fromString(cls, string):
      items = string.split("-")
      name, genre, duration = items
      movie_obj = cls(name, genre, int(duration))
      return movie_obj

    
class StarCinema:
    all_branch_info = {}
        
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.movie_list = []
        StarCinema.all_branch_info[self.branch_name] = self.movie_list
        print(f"Welcome to the {self.branch_name} branch of StarCinema! ")
        
        
  
    def addMovies(self, *movie_objects):
        movie_list = list((movie_objects))
        for i in movie_list:
            print(f"{i.name} added to {self.branch_name} branch. ")
            self.movie_list.append(i)
            StarCinema.all_branch_info[self.branch_name] = self.movie_list

    
    def removeMovie(self, movie_objects):
        if movie_objects in self.movie_list:
            self.movie_list.remove(movie_objects)
            StarCinema.all_branch_info[self.branch_name] = self.movie_list
     
    
    @classmethod
    def check(cls, movie_name):
        branches = []
        for k,v in cls.all_branch_info.items():
            branch  = k
            movies = v
            for i in movies:
                if i.name == movie_name:
                    branches.append(branch)
                    print(f"{i.name} is now streaming on {branch} branch")
                    print(i.movieInfo())
                if not branches:
                    print(f"Sorry This movie is currently not available")
                
       
    @classmethod
    def showAllBranchInfo(cls):
        for k,v in cls.all_branch_info.items():
            branch  = k
            movies = v
            print(f"Branch Name: {branch} ")
            count = 1
            for i in movies:
                print(f"Movie No: {count}")
                print(i.movieInfo())
                if count != len(movies):
                    print("#" * 50)
    

movie1 = Movie('Oppenheimer', 'Biographical Drama', 180)
print(movie1.movieInfo())
print('1==========================================')
movie2 = Movie('Barbie', 'Fantasy Comedy', 114)
print(movie2.movieInfo())
print('2==========================================')
movie3 = Movie('Spy', 'Action', 163)
print(movie3.movieInfo())
print('3==========================================')
Movie.createMovie_fromString('Prohelika-Drama-153')
print('4==========================================')
branch1 = StarCinema('Mohakhali')
print('5==========================================')
branch1.addMovies(movie1, movie2, movie3)
print('6==========================================')
StarCinema.showAllBranchInfo()
print('7==========================================')
StarCinema.check('Oppenheimer')
print('8==========================================')
movie4 = Movie.createMovie_fromString('Prohelika-Drama-153')
print(movie4.movieInfo())











# movie1 = Movie('Oppenheimer', 'Biographical Drama', 180)
# movie2 = Movie('Barbie', 'Fantasy Comedy', 114)
# movie3 = Movie('Mission: Impossible – Dead Reckoning Part One', 'Action', 163)
# print('1==========================================')
# print(movie3.movieInfo())
# print('2==========================================')
# movie4 = Movie.createMovie_fromString('Prohelika-Drama-153')
# print('3==========================================')
# print(movie4.movieInfo())
# print('4==========================================')
# branch1 = StarCinema('Mohakhali')
# print('5==========================================')
# branch1.addMovies(movie1, movie2, movie4)
# print('6==========================================')
# branch1.addMovies(movie1, movie3)
# print('7==========================================')
# StarCinema.showAllBranchInfo()
# print('8==========================================')
# branch2 = StarCinema('Mirpur')
# print('9==========================================')
# branch2.addMovies(movie1, movie2, movie3)
# print('10==========================================')
# StarCinema.showAllBranchInfo()
# print('11==========================================')
# StarCinema.check('Oppenheimer')
# print('12=========================================')
# StarCinema.check('Sound of Freedom')
# print('13=========================================')
# branch1.removeMovie(movie2)
# StarCinema.showAllBranchInfo()
# print('14=========================================')
# branch2.removeMovie(movie1)
# StarCinema.showAllBranchInfo()
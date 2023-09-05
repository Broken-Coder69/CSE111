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
      return cls(name, genre, int(duration))
  
  
    @classmethod
    def createMovie_fromString(cls, string):
        items = string.split("-")
        movie_object = cls(items)
        for question_type in items:
            obj = Movie(question_type)
            movie_object.add_questions(obj)
        return movie_object
        
        
movie4 = Movie.createMovie_fromString('Prohelika-Drama-153')
print(movie4.movieInfo())
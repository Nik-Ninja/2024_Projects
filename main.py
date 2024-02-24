class Movie:
    country_origin="India"

    def __init__(self,title,actor,actress,rating):
        self.title=title
        self.actor=actor
        self.actress=actress
        self.rating=rating

    def display_title(self):
        print(f"Our movie name is {self.title} with actors: {self.actor}")


movie1=Movie("Dear Zindagi","Shahrukh","Alia", 4.8)
movie1.display_title()
print(Movie.country_origin)
print(movie1.country_origin)

movie2=Movie("Welcome",["Uday Shetty","Majnu Bhai","Ghungaroo"],"Mallika", 5)
movie2.display_title()
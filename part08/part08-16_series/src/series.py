# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genre: list):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.ratings = []
        self.rating = 0    

    def rate(self, rating: int):        
        self.ratings.append(rating)
        self.rating = sum(self.ratings) / len(self.ratings)

    def __str__(self) -> str: 
            rating = f"no ratings" if not self.ratings else f"{len(self.ratings)} ratings, average {self.rating:.1f} points"
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genre)}\n{rating}"

def minimum_grade(rating: float, series_list: list):
     return [series for series in series_list if series.rating >= rating]
     
def includes_genre(genre: str, series_list: list):
     return [series for series in series_list if genre in series.genre]       


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

class Movie:
    def __init__(self, name, genre, length, director):
        self.name = name
        self.genre = genre
        self.length = length
        self.director = director

    def print_info(self):
        print("Movie Name:", self.name, "| Genre:", self.genre, "| Length(mins):", self.length, "| Director:", self.director)

    def change_director(self, new_director):
        self.director = new_director

    def calculate_length(self):
        h = self.length // 60.
        m = self.length % 60.
        print("This movie is ", h, " hours and ", m, " minutes long")
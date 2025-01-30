from classes import Movie

movie1 = Movie("Finding Nemo", "Family/Adventure", 100, "Andrew Stanton") #instantiating a movie
movie1.print_info() #printing the original info
movie1.calculate_length() #printing the movie length in hours and minutes
movie1.change_director("Daniel Strokin") #changing the director
movie1.print_info() #showing the new info

print("\n") #seperating the classes to make it clearer in terminal

movie2 = Movie("The Hateful Eight", "Western", 187, "Quentin Tarantino") #instantiating a new movie
movie2.print_info() #printing the original info
movie2.calculate_length() #printing the movie length in hours and minutes
movie2.change_director("Daniel Strokin") #changing the director
movie2.print_info() #showing the new info

#comment for merge
"""
Entertainment Center is a module were Movie instances are created and added to
a list; 'movies'. This list is then passed onto the 'fresh_tomatoes' module
which outputs an html file to the local folder. This html is then opened in
the default web browser of the system.
"""

import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story", "1995",
    "A story of a boy and his toys that come to life.",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

school_of_rock = media.Movie("School of Rock", "2003",
    "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown \
    out of his bar band and finds himself in desperate need of work.",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", # noqa
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

the_imitation_game = media.Movie(
    "The Imitation Game", "2014",
    "In 1939, newly created British intelligence agency MI6 recruits \
    Cambridge mathematics alumnus Alan Turing (Benedict Cumberbatch) to \
    crack Nazi codes, including Enigma",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQQ5vi9xgRkP0nk5aRn8tcGEGRnOQyM-aAS1ldqfQSi_69V1yfU", # noqa
    "https://www.youtube.com/watch?v=S5CjKEFb-sM")

whiplash = media.Movie(
    "Whiplash", "2014",
    "Andrew Neiman (Miles Teller) is an ambitious young jazz drummer, \
    in pursuit of rising to the top of his elite music conservatory.",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcS_IwW5-_mWA1PXiPG4qEhLC6Q3vntQd7Bzgs_YE7HHFifItn2T", # noqa
    "https://www.youtube.com/watch?v=7d_jQycdQGo")

# List of movie instances
movies = [toy_story, school_of_rock, the_imitation_game, whiplash]
# Rendering the html file by passing movies to the fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
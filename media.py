import webbrowser

class Movie():
    """
    The "Movie" class represents a movie object with the following attributes:
    Args:
        param1(string): Title
        param2(int): Release Year
        param3(string): Storyline
        param4(string): Poster Image URL
        param5(string): Trailer Youtube URL
    """
    def __init__(self, movie_title, movie_release_year, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = movie_release_year

    def show_trailer(self):
    	"""
    	Opens the trailer url in the default web browser.
    	"""
        webbrowser.open(self.trailer_youtube_url)
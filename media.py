import webbrowser


class Movie():

    """
    class Movie:
        represents a movie objets
        Args:
        title = a string of the movie's title
        year = an integer for the year of the movie's release
        poster_url = a string containing a URL to a poster image
        trailer_url = a string containing a youtube URL of the movie's trailer
        """
    def __init__(
            self, movie_title,
            movie_story_line, poster_image,
            trailer_youtube):

        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie():
    """class Movie contain movie information """
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """first : movie title - second story line - third : poster url - finally youtube url  """
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

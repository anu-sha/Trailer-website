class Movie():
    """This class provides a way to store movie related information such as the tile, brief storyline
         poster url and trailer url"""
    
    """The movie class initializer accepts the movie tile
       storyline, poster url and the trailer url""" 
    def __init__(self,title,storyline,image_url,trailer_url):
        self.title=title
        self.storyline=storyline
        self.image_url=image_url
        self.trailer_url=trailer_url

    

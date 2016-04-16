#importing the file that defines the movie class and the file that generates the html
import media
import fave_trailers

#Initializing movie objects

#baahubali movie object
baahubali=media.Movie("Baahubali",
                   "The story of Mahishmati kingdom",
                   "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                   "https://www.youtube.com/watch?v=3NQRhE772b0")

#bangalore days movie object
bloredays = media.Movie("Bangalore Days",
                        "A story of three cousins who set out to fulfill their dreams",
                        "https://upload.wikimedia.org/wikipedia/en/5/5c/%27Bangalore_Days%27_2014_Malayalam_Film_-_Poster.jpg",
                        "https://www.youtube.com/watch?v=c4Li7aET3Y4")

#ohm shanthi oshana movie object
oshana=media.Movie("Ohm Shanthi Oshana",
                   "Story of Pooja and Girish",
                   "https://upload.wikimedia.org/wikipedia/en/a/ae/Ohm_Shanthi_Oshaana_%282014%29_-_Poster.jpg",
                   "https://www.youtube.com/watch?v=GaznvwVEED4")

#three idiots movie object
threeidiots=media.Movie("Three Idiots",
                   "A story of three friends",
                   "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                   "https://www.youtube.com/watch?v=xvszmNXdM4w")

#athadu movie object
athadu=media.Movie("Athadu",
                   "The story of a professional killer",
                   "https://upload.wikimedia.org/wikipedia/en/e/ee/Athadu_Poster.jpg",
                   "https://www.youtube.com/watch?v=zWR28TzH1Fs")

#yennai arindhaal movie object
yennai=media.Movie("Yennai Arindhaal",
                   "The story of a cop",
                   "https://upload.wikimedia.org/wikipedia/en/4/4d/Yennai_Arindhaal.jpg",
                   "https://www.youtube.com/watch?v=B7c87SWQg-Y")

#adding all movie objects to a list
movies=[baahubali,bloredays,oshana,threeidiots,athadu,yennai]

#calling the open movies page method in fave_trailers that takes the movie objects list to generate the trailer web page
fave_trailers.open_movies_page(movies)



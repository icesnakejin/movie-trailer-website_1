import fresh_tomatoes
import media

# instances of movies
toy_story = media.Movie("Toy story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", "https://www.youtube.com/watch?v=d1_JBMrrYw8")
harrypotter = media.Movie("Harry Potter", "A story of a boy who becomes a wizard and save the world", "http://ia.media-imdb.com/images/M/MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=czFqCdNRHqQ")
forrestgump = media.Movie("Forrest Gump", "The story depicts several decades in the life of Forrest Gump", "http://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg","https://www.youtube.com/watch?v=uPIEn0M8su0")
thelordoftherings = media.Movie("The Lord of The Rings", "The magic ring that causes the war of the world", "http://img2.wikia.nocookie.net/__cb20070806215413/lotr/images/8/87/Ringstrilogyposter.jpg","https://www.youtube.com/watch?v=V75dMMIW2B4")
shawshankredemption = media.Movie("Shawshank redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency(imdb)", "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

# list of movie instances
movies = [toy_story,avatar, harrypotter, forrestgump, thelordoftherings, shawshankredemption]

# form html file and open in the browser
fresh_tomatoes.open_movies_page(movies)

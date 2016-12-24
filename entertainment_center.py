import fresh_tomatoes
from media import  Movie
dark_knight= Movie("The Dark knight",
                " When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice. ",
               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
               "https://www.youtube.com/watch?v=EXeTwQWrcwY")


blood_diamond= Movie("Blood Diamond",
                     " A fisherman, a smuggler, and a syndicate of businessmen match wits over the possession of a priceless diamond. ",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIwNDEzNTY2NV5BMl5BanBnXkFtZTgwNjAyMDAxMzE@._V1_.jpg",
                     "https://www.youtube.com/watch?v=XtPX2kXhu7I")

django= Movie("Django Unchained",
" A fisherman, a smuggler, and a syndicate of businessmen match wits over the possession of a priceless diamond. ",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=eUdM9vrCbow")

revenant= Movie("the revenant"," A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team. ",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BY2FmODc2N2QtYmY3MS00YTMwLWI2NGYtZWRmYWVkNjFjZmI0XkEyXkFqcGdeQXVyNTMxMjgxMzA@._V1_.jpg",
                "https://www.youtube.com/watch?v=LoebZZ8K5N0")


guardians_of_the_galaxy= Movie("Guardians of the Galaxy",
                               " A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe. ",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=89q_HH-3ghk")

zootopia= Movie("Zootopia"," In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy. ",
"https://images-na.ssl-images-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_SY1000_SX675_AL_.jpg",
                "https://www.youtube.com/watch?v=c6rP-YP4c5I")

movies_list = []
movies_list.append(dark_knight)
movies_list.append(django)
movies_list.append(guardians_of_the_galaxy)
movies_list.append(revenant)
movies_list.append(blood_diamond)
movies_list.append(zootopia)
fresh_tomatoes.open_movies_page(movies_list)

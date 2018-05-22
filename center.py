import media
import fresh_tomatoes


AIW = media.movie(
    "Avengers Infinity War",
    "Stopping Thanos",
    "https://bit.ly/2rZ9HDT",
    "https://youtu.be/6ZfuNTqbHE8")
W_W = media.movie(
    "Wonder Woman", "Brave lady",
    "https://bit.ly/2IXVMre",
    "https://youtu.be/VSB4wGIdDwo")
B_B = media.movie("Boss Babby",
                  "Kid from business school",
                  "https://bit.ly/2LjBo20",
                  "https://youtu.be/h24gEn3y82Q")
CROODS = media.movie(
    "THE Croods", "Cave man Life",
    "https://bit.ly/2IAPJW6",
    "https://youtu.be/4fVCKy69zUY")
FROZEN = media.movie(
    "FROZEN", "Finding sister",
    "https://bit.ly/2x3yrQc",
    "https://youtu.be/TbQm5doF_Uc")
T_J = media.movie(
    "Tom and Jerry", "Land of OZ",
    "https://bit.ly/2ICfucL",
    "https://youtu.be/tyE8XnZBJQA")
movies = [AIW, W_W, B_B, CROODS, FROZEN, T_J]
fresh_tomatoes.open_movies_page(movies)

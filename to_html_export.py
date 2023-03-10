import pandas as pd
from Reservatiesysteem import *

#testcodes
import Reservatiesysteem
from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *

from Reservatiesysteem import *
r = Reservatiesysteem()

print()
r.addGebruiker(1,"sejar","dindar","sejar@10")
print()
r.addFilm(1,"The Matrix",6.1)
print()
r.addFilm(2,"Inception",7.1)
print()
r.addReservatie(1,"TG","12","1","4")
print()
r.addVertoning(1,20,4,"2 oktober", 1)
print()
r.addZaal(10,200)
print()
r.addVertoning(1,20,4,"2 oktober", 1)



my_dict = {
    'MOVIE': [r.films.retrieve(1)[0].zoek_film(1),r.films.retrieve(2)[0].zoek_film(2),'Maze Runner'],
    'ID': [r.films.retrieve(1)[0].id, 2, 3],
    'TIJD': [30, 40, 50],
    'ZAAL': [1, 2, 3]
}
my_data = pd.DataFrame(data=my_dict)
my_data.to_html('C:/Users/aboba/PycharmProjects/MainTOg/abu.html',index = False)

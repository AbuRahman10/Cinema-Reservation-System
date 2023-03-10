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
r.addFilm(3,'Maze Runner',4.3)
print()
r.addReservatie(1,"TG","12","1","4")
print()
r.addVertoning(1,20,4,"2 oktober", 1)
print()
r.addZaal(10,200)
print()
r.addVertoning(1,20,4,"2 oktober", 1)

filmlist = []
idlist = []
i = 1
while i <= r.films.getLength():
    filmlist.append(r.films.retrieve(i)[0].zoek_film(i))
    idlist.append(i)
    i+=1

my_dict = {
    'MOVIE': filmlist,
    'ID': idlist,
    'TIJD': [30, 40, 50],
    'ZAAL': [1, 2, 3]
}
my_data = pd.DataFrame(data=my_dict)
my_data.to_html('C:/Users/aboba/PycharmProjects/MainTOg/abu.html',index = False)
